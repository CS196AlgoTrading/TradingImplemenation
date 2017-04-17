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

def buyOrSell(ticker):
    while True:
        point = 0
        increase = 0
        decrease = 0
        while point <= 50:
            if compareToAvg(prices):
                increase += 1
            else:
                decrease += 1
            yield (increase >= decrease) #sell stocks Otherwise, buy stocks
            point += 1
