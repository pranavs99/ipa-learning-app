from ipa_learning_app.sound import Sound

# the Vowel class defines an IPA symbol typically distinguished
# by its height, backness, and rounding
class Vowel(Sound):

    # constructor
    def __init__(self, symbol, height, backness, rounding):
        # inheriting all fields and methods from the parent class, Sound
        # all Vowel objects have the .phonation set to "voiced"
        # and .airstream set to "pulmonic"
        super().__init__(
            symbol = symbol,
            phonation = "voiced",
            airstream = "pulmonic",
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
