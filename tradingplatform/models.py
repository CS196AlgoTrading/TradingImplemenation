import getopt
import sys
import Streamer

def compareToAvg(prices):
    # Yields true if increasing, false if decreasing
    historic = 0
    i = 0
    total = 0
    for price in prices:
        i += 1
        total += price
        historic = total/i
        yield (price>historic)

def buyOrSell(ticker, prices):
    point = 0
    increase = 0
    decrease = 0
    while point <= 50: #check 50 points of the average to decide
        if compareToAvg(prices):
            increase += 1
        else:
            decrease += 1
        point += 1
    yield (increase >= decrease) #sell stocks Otherwise, buy stocks

def main(argv):
    fileName = ""
    holdingStock = 0
    ticker = ""
        try:
            opts, args = getopt.getopt(argv,"ht:h:p:,["ticker=","holdingStock=", "profit="])
        except getopt.GetoptError:
            print ('models.py -t <ticker> -a <amount> -p <profit>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('models.py -t <ticker> -a <amount> -p <profit>')
                sys.exit()
            elif opt in ("-t", "--ticker"):
                ticker = arg
            elif opt in ("-h", "--amount"):
                print("amount of holding stocks:", holdingStock)
            elif opt in ("-p", "--profit"):
                print("current profit:", profit)

    streamer = Streamer(ticker, fileName)
    prices = streamer.stream()

    while(holdingStock > -1):
        if buyOrSell(ticker,prices):
            holdingStock += 100
            profit -= holdingStock * prices * 1.1
        else:
            profit += holdingStock * prices * 0.9
            holdingStock = 0


if __name__ == "__main__":
    main(sys.argv[1:])
