# the Consonant class defines an IPA symbol typically distinguished
# by its place, manner, phonation, and airstream
class Consonant:

    # constructor
    def __init__(self, symbol, place, manner, phonation, airstream):
        self.symbol = symbol
        self.place = place
        self.manner = manner
        self.phonation = phonation
        self.airstream = airstream

    # accessors
    def get_symbol(self):
        return self.symbol
    def get_place(self):
        return self.place
    def get_manner(self):
        return self.manner
    def get_phonation(self):
        return self.phonation
    def get_airstream(self):
        return self.airstream