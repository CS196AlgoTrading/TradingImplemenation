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
