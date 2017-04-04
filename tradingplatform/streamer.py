import json
# Streamer has a ticker symbol and an input file
# It exposes the function `stream` which calls
# reads the input file and yields the data as
# Python objects and primitives until the input
# file terminates
class Streamer:
    def __init__(self, ticker, input_file):
        self.ticker = ticker
        self.input_file = input_file

    # stream opens the input file and continually
    # tries to read data from it. If data is read,
    # it is yielded as a Python object or primitive.
    # This function returns when the input file is
    # closed.
    def stream(self):
        with open(self.input_file,"r") as f:
            for line in f:
                data=f.read()
                f.close() 
                
        j_object=json.load({data})
        output=json.dump(j_object,)
        pass
    
def main():
    # implement the code to parse command-line arguments,
    # create a Listener based on those arguments,
    # and start streaming the data
    pass

if __name__ == "__main__":
    main()
