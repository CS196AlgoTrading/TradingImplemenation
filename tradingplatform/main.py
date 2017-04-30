import tradingplatform
import sys
import getopt
import tradingplatform.models
from tradingplatform.streamer import Streamer
from tradingplatform.listener import Listener
from yahoo_finance import Share

def main(argv):
    # implement the code to parse command-line arguments,
    # combine listner, streamer, and models together

    ticker = ''
    frequency = 0.0
    fileName = ''

    try:
        opts, args = getopt.getopt(argv, "ht:f:",["ticker=","frequency="])
    except  getopt.GetoptError:
        print("main.py -t <ticker> -f <frequency>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("main.py -t <ticker> -f <frequency>")
            sys.exit()
        elif opt in ("-t", "--ticker"):
            ticker = arg
        elif opt in ("-f","--frequency"):
            frequency = float(arg)

    fileName = ticker + ".txt"

    writer = tradingplatform.listener.PriceListener(ticker, fileName)
    writer.listen(frequency)

    trader = models(ticker, fileName)

if __name__ == "__main__":
    main(sys.argv[1:])
