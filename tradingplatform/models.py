def compareToAvg(prices):
    # Yields true if increasing, false if decreasing
    historic = 0
    i = 0
    total = 0
    for price in prices:
        i = i + 1
        total = total + price
        historic = total/i
        if (price>historic):
            yield True
        else:
            yield False
