import getopt
import sys
<<<<<<< HEAD
import time
from streamer import Streamer

totalnumber = 0
historictotal = 0
averageprice = 0

def compareToAvg(price):
    # Yields true if increasing, false if decreasing
    global totalnumber
    global historictotal
    global averageprice
    averageprice = historictotal/totalnumber
    indicator = price > averageprice
    totalnumber += 1
    historictotal += price
    return indicator

def tradingAmount(ticker):
    global averageprice
    while(True){
    fileName = ticker + ".txt"
    reader = Streamer(ticker, fileName)
    price = reader.stream();
    if compareToAvg(price):
        return price
    else if price < averageprice:
        return (0 - price)
    time.sleep(10)
    }
=======
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
>>>>>>> origin

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
<<<<<<< HEAD
        if price > 0:
            holdingStock += 100
            profit -= holdingStock * price * 1.1
        else:
            profit -= holdingStock * price * 0.9
=======
        if holdingStock == 0 or price < 0:
            holdingStock += 100
            profit -= holdingStock * price * 1.1
        else:
            profit += holdingStock * price * 0.9
>>>>>>> origin
            holdingStock = 0
        print("amount of holding stocks: %d \tcurrent profit: %f" %(holdingStock,profit))

if __name__ == "__main__":
    main(sys.argv[1:])
