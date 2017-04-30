import sys
import getopt
import listener
from yahoo_finance import Share
# Streamer has a ticker symbol and an input file
# It exposes the function `stream` which calls
# reads the input file and yields the data as
# Python objects and primitives until the input
# file terminates
class Streamer:
    def __init__(self, ticker, input_file):
        self.ticker = ticker
        self.input_file = input_file

    # stream opens the input file and read the last_line.
    #  It will return a Python object or primitive.

    def stream(self):
        with open(self.input_file, 'R') as info:
            lines = info.read().splitlines()
            last_line = lines[-1]
            date, ticker, price = last_line.split('\t')
            return date,ticker,float(price)


def main(argv):
    # implement the code to parse command-line arguments,
    # create a Listener based on those arguments,
    # and start streaming the data
    filename = None
    ticker = ""
    try:
        opts, args = getopt.getopt(argv,"ht:",["ticker="])
    except getopt.GetoptError:
        print('streamer.py -t <ticker>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("streamer.py -t <ticker>")
            sys.exit()
        elif opt in ("-t", "--ticker"):
            ticker = arg
    filename = ticker + ".txt"
    streamer = Streamer(ticker, filename)
    for t in streamer.stream(): # t for tuple
        print(t)

if __name__ == "__main__":
    main(sys.argv[1:])
