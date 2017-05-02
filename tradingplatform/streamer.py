from yahoo_finance import Share
# Streamer has a ticker symbol and an input file
# It exposes the function `stream` which calls
# reads the input file and yields the data as
# Python objects and primitives until the input
# file terminates
class Streamer:
    def __init__(self, ticker):
        self.ticker = ticker
        self.input_file = ticker + ".txt"

    # stream opens the input file and continually
    # tries to read data from it. If data is read,
    # it is yielded as a Python object or primitive.
    # This function returns when the input file is
    # closed.
    def stream(self):
        with open(self.input_file, 'r') as info:
            for line in info:
                date, ticker, price = line.split('\t')
                yield date,ticker,float(price)
