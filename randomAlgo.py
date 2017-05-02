import sys
import getopt
from tradingplatform.streamer import Streamer
from yahoo_finance import Share
from random import randint

def random(prices):
    holdingStock = 0
    profit = 0.0
    currentpoint = 0
    while(currentpoint < len(prices)):
        buyOrSell = randint(0,1)
        if buyOrSell==1 or holdingStock == 0:
            stock = randint(0,100)
            holdingStock += stock
            profit -= 1.1 * stock * prices[currentpoint]
        else:
            stock = randint(0,holdingStock)
            holdingStock -= stock
            profit += 0.9 * stock * prices[currentpoint]
        currentpoint += 1
        print("amount of holding stocks: %d\tcurrent profit: %f" %(holdingStock,profit))


def main(argv):

    ticker = ''
    prices = []

    try:
        opts, args = getopt.getopt(argv, "ht:",["ticker="])
    except getopt.GetoptError:
        print("random.py -t <ticker>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("random.py -t <ticker>")
            sys.exit()
        elif opt in ("-t", "--ticker"):
            ticker = arg

    reader = Streamer(ticker)
    for t in reader.stream():
        prices.append(t[2])
    random(prices)

if __name__ == '__main__':
    main(sys.argv[1:])
