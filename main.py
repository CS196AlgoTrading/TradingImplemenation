import tradingplatform
import sys
import getopt
from tradingplatform import models
from tradingplatform.streamer import Streamer
from yahoo_finance import Share

def main(argv):
    # implement the code to parse command-line arguments,
    # combine listner, streamer, and models together

    ticker = ''
    prices = [0.0]

    try:
        opts, args = getopt.getopt(argv, "ht:",["ticker="])
    except  getopt.GetoptError:
        print("main.py -t <ticker>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("main.py -t <ticker>")
            sys.exit()
        elif opt in ("-t", "--ticker"):
            ticker = arg

    reader = Streamer(ticker)
    for t in reader.stream():
        prices.append(t[2])
    models.trade(prices[1:])

if __name__ == "__main__":
    main(sys.argv[1:])
