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

    # stream opens the input file and continually
    # tries to read data from it. If data is read,
    # it is yielded as a Python object or primitive.
    # This function returns when the input file is
    # closed.
    def stream(self):
            with open(self.input_file, 'R') as info:
                for line in info:
                    date, ticker, price = line.split('\t')
                    yield date,ticker,float(price)


def main(argv):
    # implement the code to parse command-line arguments,
    # create a Listener based on those arguments,
    # and start streaming the data
    filename = None
    try:
        opts, args = getopt.getopt(argv,"hl",["listener"])
    except getopt.GetoptError:
        print('streamer.py -f <filename>')
        sys.exit(2)
    for opt.arg in opts:
        if opt == '-h':
            print ("streamer.py -f <filename>")
        elif opt in ("-f", "--filename"):
            filename = arg

    streamer = Streamer(filename)
    for t in streamer.stream(): # t for tuple
        print(t)

if __name__ == "__main__":
    main(sys.argv[1:])
