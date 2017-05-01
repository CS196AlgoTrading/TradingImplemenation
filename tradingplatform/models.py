import getopt
import sys
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

# It will continue to get value from streamer until there is a decision buy or sell
# made.
def tradingAmount(ticker):
    global averageprice
    while(True){
    fileName = ticker + ".txt"
    reader = Streamer(ticker, fileName)
    price = reader.stream()[2];
    if compareToAvg(price):
        return price
    else if price < averageprice:
        return (0 - price)
    time.sleep(10)
    }

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
        if price > 0:
            holdingStock += 100
            profit -= holdingStock * price * 1.1
        else:
            holdingStock -= 100
            profit -= holdingStock * price * 0.9
        
        print("amount of holding stocks: %d \tcurrent profit: %f" %(holdingStock,profit))

if __name__ == "__main__":
    main(sys.argv[1:])
