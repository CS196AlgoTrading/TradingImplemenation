import getopt
import sys

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
    while True:
        point = 0
        increase = 0
        decrease = 0
        while point <= 50: #check 50 points of the average to decide
            if compareToAvg(prices):
                increase += 1
            else:
                decrease += 1
            yield (increase >= decrease) #sell stocks Otherwise, buy stocks
            point += 1

def main(argv):
    fileName = ""
    holdingStock = 0
    ticker = ""
        try:
            opts, args = getopt.getopt(argv,"ht:h:p:f:,["ticker=","holdingStock=", "profit=","fileName="])
        except getopt.GetoptError:
            print ('models.py -t <ticker> -a <amount> -p <profit> -f <file name>')
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
            elif opt in ("-f","--file name"):
                fileName = argv

    while(holdingStock > -1):
        if buyOrSell(ticker,prices):
            holdingStock += 100
            profit -= holdingStock * prices
        else:
            profit += holdingStock * prices
            holdingStock = 0


if __name__ == "__main__":
    main(sys.argv[1:])
