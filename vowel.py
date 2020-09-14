class Vowel:

    # constructor
    def __init__(self, symbol, height, backness, rounding):
        self.symbol = symbol
        self.height = height
        self.backness = backness
        self.rounding = rounding
    
    # accessors
    def get_symbol(self):
        return self.symbol
    def get_height(self):
        return self.height
    def get_backness(self):
        return self.backness
    def get_rounding(self):
        return self.rounding