# Listener has a ticker symbol and an output file
# It exposes the function `listen` which calls
# checkUpdate every `frequency` seconds and writes
# the latest data to an output file

import time
import sys
import getopt
from yahoo_finance import Share

class Listener:
    def __init__(self, ticker, output_file):
        self.ticker = ticker
        self.output_file = output_file

    # checkUpdate is an abstract method that
    # should be implemented by all subclasses
    def checkUpdate(self):
        # do not change this
        raise NotImplementedError

    # listen checks for updates and writes them to
    # the output file every `frequency` seconds
    def listen(self, frequency):
        while(True):
            time.sleep(frequency)
            out = self.checkUpdate()
            with open(self.output_file, 'a') as output:
                output.write('\t'.join('%s'%x for x in out)+"\n")

# PriceListener extends Listener
# Its checkUpdate function gets the latest price
class PriceListener(Listener):
    def __init__(self, ticker, output_file):
        super().__init__(ticker, output_file)

    # checkUpdate gets the latest price
    # using the yahoo-finance library
    # and writes the data to self.output_file
    def checkUpdate(self):
        myShare = Share(self.ticker)
        return myShare.get_trade_datetime(), self.ticker, myShare.get_price()


def main(argv):
    # implement the code to parse command-line arguments,
    # create some sort of Listener based on those,
    # and start listening
    ticker = ''
    frequency = 1
    outputFile = ''

    try:
        opts, args = getopt.getopt(argv,"ht:f:o:",["ticker=","frequency=", "ofile="])
    except getopt.GetoptError:
        print ('listener.py -t <ticker> -f <frequency> -o <outputFile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('listener.py -t <ticker> -f <frequency> -o <outputFile>')
            sys.exit()
        elif opt in ("-t", "--ticker"):
            ticker = arg
        elif opt in ("-f", "--frequency"):
            frequency = int(arg)
        elif opt in ("-o", "--ofile"):
            outputFile = arg




    listener = PriceListener(ticker, outputFile)
    listener.listen(frequency)

if __name__ == "__main__":
    main(sys.argv[1:])
