from ipa_sound import IPASound

# the Consonant class defines an IPA symbol typically distinguished
# by its place, manner, phonation, and airstream
class Consonant(IPASound):

    # constructor
    def __init__(self, symbol, place, manner, phonation, airstream):
        # inheriting all fields and methods from the parent class IPASound
        super().__init__(
            symbol = symbol,
            phonation = phonation,
            airstream = airstream
        )
        # adding Consonant-specific fields
        self.place = place
        self.manner = manner

    # Consonant-specific accessors
    def get_place(self):
        return self.place
    def get_manner(self):
        return self.manner