import unittest
from ipa_learning_app.ipa_sound import IPASound

# testing the IPASound object
class TestIPASoundClass(unittest.TestCase):

    # valid IPASound() arguments
    valid_symbol = 'p'
    valid_phonation = "unvoiced"
    valid_airstream = "pulmonic"

    # invalid IPASound() arguments
    invalid_symbol = '2'
    invalid_phonation = "numeric"
    invalid_airstream = "mathematical"

    # testing with valid arguments
    def test_creation_with_valid_arguments(self):
        s = IPASound(
            symbol = self.valid_symbol,
            phonation = self.valid_phonation,
            airstream = self.valid_airstream
        )
        self.assertEqual(s.get_symbol(), self.valid_symbol)
        self.assertEqual(s.get_phonation(), self.valid_phonation)
        self.assertEqual(s.get_airstream(), self.valid_airstream)

    # testing with valid arguments
    def test_creation_with_invalid_arguments(self):
        pass