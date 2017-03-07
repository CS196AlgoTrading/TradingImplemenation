# Listener has a ticker symbol and an output file
# It exposes the function `listen` which calls
# checkUpdate every `frequency` seconds and writes
# the latest data to an output file
class Listener:
    def __init__(self, ticker, output_file):
        self.ticker = ticker
        self.output_file = output_file

    # checkUpdate is an abstract method that
    # should be implemented by all subclasses
    def checkUpdate(self):
        # do not change this
        raise NotImplementedError

    # listen checks for updates and writes them to
    # the output file every `frequency` seconds
    def listen(self, frequency):
        # implement this
        pass

# PriceListener extends Listener
# Its checkUpdate function gets the latest price
class PriceListener(Listener):
    def __init__(self, ticker, output_file):
        super().__init__(self, ticker, output_file)

    # checkUpdate gets the latest price
    # using the yahoo-finance library
    # and writes the data to self.output_file
    def checkUpdate(self):
        # implement this
        # print(some_string, file=self.output_file) will be useful
        pass

def main():
    # implement the code to parse command-line arguments,
    # create some sort of Listener based on those,
    # and start listening
    pass

if __name__ == "__main__":
    main()
