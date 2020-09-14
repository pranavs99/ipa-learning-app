# the Vowel class defines an IPA symbol typically distinguished
# by its height, backness, and rounding
class Vowel:

    # constructor
    def __init__(self, symbol, height, backness, rounding):
        self.symbol = symbol
        self.height = height
        self.backness = backness
        self.rounding = rounding
        # all vowels are voiced and pulmonic by default
        self.phonation = "voiced"
        self.airstream = "pulmonic"
    
    # accessors
    def get_symbol(self):
        return self.symbol
    def get_height(self):
        return self.height
    def get_backness(self):
        return self.backness
    def get_rounding(self):
        return self.rounding
    def get_phonation(self):
        return self.phonation
    def get_airstream(self):
        return self.airstream