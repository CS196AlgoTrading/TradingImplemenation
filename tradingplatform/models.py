historic = 0
def compareToAvg(prices):
    # Yields true if increasing, false if decreasing
    number = 0
    total = 0
    for price in prices:
        number += 1
        total += price
        historic = total/number
        yield (price > historic * 1.1)

def buyOrSell(prices):
    increase = 0
    currentPrice = 0.0
    decrease = 0
    lastPrice = 0
    for point in range (50): #check 50 points of the average to decide
        if point >= len(prices):
            break
        if compareToAvg(prices):
            increase += 1
        else:
            decrease += 1
        lastPrice = prices[point]
    if(increase > decrease):
        currentPrice = lastPrice
    return currentPrice

def trade(prices):
    holdingStock = 0.0
    profit = 0.0

    while(holdingStock > -1):
        price = buyOrSell(prices)
        if holdingStock == 0.0 or price < 0:
            holdingStock += 100.0
            profit -= holdingStock * price * 1.1
        else:
            profit += holdingStock * price * 0.9
            holdingStock = 0
        print("amount of holding stocks: %d\tcurrent profit: %f" %(holdingStock,profit))
