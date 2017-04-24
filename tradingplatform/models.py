
class models:
    def __init__():
        self.decisionScore = 0

    def compareToAvg(currentprice,historicData):
    # return true if increasing, false if decreasing
        i = 0
        total = 0
        for price in historicData:
            total += price

        historic = total/(len(historicData))
        return (currentprice > historic)

    def makeDecision():

        if compareToAvg(currentprice,historicData):
            decisionScore += 1
        else:
            decisionScore += 1

        if decisionScore > 5 :
            return "buy in"
