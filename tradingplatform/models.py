from random import randint

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
    if(increase > decrease): #sell stocks
        return lastPrice
    return 0.0 - lastPrice

def trade(prices):
    holdingStock = 0
    profit = 0.0
    count = 0
    while count < len(prices):
        price = buyOrSell(prices)
        if price < 0:
            holdingStock -= int(999/price)
            profit -= holdingStock * price * 1.1
        elif holdingStock == 0:
            holdingStock += randint(0,20)
            profit -= holdingStock * price * 1.1
        else:
            stock = randint(0,holdingStock)
            profit += stock * price * 0.9
            holdingStock -= stock
        print("amount of holding stocks: %d\tcurrent profit: %f" %(holdingStock,profit))
        count += 1
