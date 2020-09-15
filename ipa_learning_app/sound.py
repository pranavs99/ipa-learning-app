# the Sound class is a parent class for Vowel and Consonant because
# both of these classes share a few fields and methods
class Sound:

    # constructor
    def __init__(self, symbol, phonation, airstream):
        self.symbol = symbol
        self.phonation = phonation
        self.airstream = airstream

    # accessors
    def get_symbol(self):
        return self.symbol
    def get_phonation(self):
        return self.phonation
    def get_airstream(self):
        return self.airstream