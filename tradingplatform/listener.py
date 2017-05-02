# Listener has a ticker symbol and an output file
# It exposes the function `listen` which calls
# checkUpdate every `frequency` seconds and writes
# the latest data to an output file

import time
from yahoo_finance import Share

class Listener:
    def __init__(self, ticker):
        self.ticker = ticker
        self.output_file = ticker + ".txt"

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
    def __init__(self, ticker):
        super().__init__(ticker)

    # checkUpdate gets the latest price
    # using the yahoo-finance library
    # and writes the data to self.output_file
    def checkUpdate(self):
        myShare = Share(self.ticker)
        return myShare.get_trade_datetime(), self.ticker, myShare.get_price()
