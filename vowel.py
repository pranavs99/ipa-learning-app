from ipa_sound import IPASound

# the Vowel class defines an IPA symbol typically distinguished
# by its height, backness, and rounding
class Vowel(IPASound):

    # constructor
    def __init__(self, symbol, height, backness, rounding):
        # inheriting all fields and methods from the parent class, IPASound
        # and setting the .phonation & .airstream fields because they're the
        # same for all consonant
        super().__init__(
            symbol = symbol,
            # all vowels are voiced
            phonation = "voiced",
            # all vowels are pulmonic
            airstream = "pulmonic"
        )
        # Vowel-specific fields
        self.height = height
        self.backness = backness
        self.rounding = rounding
    
    # Vowel-specific accessors
    def get_height(self):
        return self.height
    def get_backness(self):
        return self.backness
    def get_rounding(self):
        return self.rounding