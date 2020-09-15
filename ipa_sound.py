import unittest

# the IPASound class is a parent class for Vowel and Consonant because
# both of these classes share a few fields and methods
class IPASound:

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



# testing the IPASound object
class TestIPASoundClass(unittest.TestCase):

    # testing fields
    dummy_symbol = "p"
    dummy_phonation = "unvoiced"
    dummy_airstream = "pulmonic"

    def test_creation_with_valid_arguments(self):
        s = IPASound(
            symbol = self.dummy_symbol,
            phonation = self.dummy_phonation,
            airstream = self.dummy_airstream
        )
        self.assertEqual(s.get_symbol(), self.dummy_symbol)
        self.assertEqual(s.get_phonation(), self.dummy_phonation)
        self.assertEqual(s.get_airstream(), self.dummy_airstream)

    def test_creation_with_invalid_arguments(self):
        pass