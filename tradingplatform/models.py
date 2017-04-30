import getopt
import sys
from streamer import Streamer

historic = 0
def compareToAvg(prices):
    # Yields true if increasing, false if decreasing
    number = 0
    total = 0
    for price in prices:
        number += 1
        total += price
        historic = total/number
        yield (price>historic)

def tradingAmount(ticker):
    increase = 0
    decrease = 0
    currentPrice = -1
    prices = []
    fileName = ticker + ".txt"
    reader = Streamer(ticker, fileName)
    for t in reader.stream(): # t for tuple
        prices.append(t[2])
    for point in range (50): #check 50 points of the average to decide
        if compareToAvg(prices):
            increase += 1
        else:
            decrease += 1
    if(increase > decrease):
        currentPrice = prices[len(prices)-1]
    return currentPrice

def main(argv):
    fileName = ""
    holdingStock = 0
    ticker = ""
    profit = 0.0
    try:
        opts, args = getopt.getopt(argv,"ht:",["ticker="])
    except getopt.GetoptError:
        print ('models.py -t <ticker>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('models.py -t <ticker>')
            sys.exit()
        elif opt in ("-t", "--ticker"):
            ticker = arg

    while(holdingStock > -1):
        price = tradingAmount(ticker)
        if holdingStock == 0 or price < 0:
            holdingStock += 100
            profit -= holdingStock * price * 1.1
        else:
            profit += holdingStock * price * 0.9
            holdingStock = 0
        print("amount of holding stocks: %d \tcurrent profit: %f" %(holdingStock,profit))

if __name__ == "__main__":
    main(sys.argv[1:])
