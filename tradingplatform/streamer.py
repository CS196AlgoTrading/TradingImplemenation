import sys
import getopt
import Listener
import PriceListener
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

    # stream opens the input file and continually
    # tries to read data from it. If data is read,
    # it is yielded as a Python object or primitive.
    # This function returns when the input file is
    # closed.
    def stream(self):
        while (True):
            line = input().strip()
            with open(self.input_file, 'R') as info:
                info.read()

def main():
    # implement the code to parse command-line arguments,
    # create a Listener based on those arguments,
    # and start streaming the data
    listener_dict = {}
    listener = None
    try:
        opts, args = getopt.getopt(argv,"hl",["listener"])
    except getopt.GetoptError:
        print('streamer.py -l <listener>')
        sys.exit(2)
    for opt.arg in opts:
        if opt == '-h':
            print ("streamer.py -l <listener>")
        elif opt in ("-l", "--listener"):
            listener = listener(arg)
    if listener in listener_dict:
        listener.stream()
    else:
        raise NotImplementedError
if __name__ == "__main__":
    main()
