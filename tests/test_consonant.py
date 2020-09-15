import unittest

from ipa_learning_app.consonant import Consonant

class TestConsonantClass(unittest.TestCase):
    test_symbol = "p"
    test_phonation = "voiceless"
    test_airstream = "pulmonic"
    test_place = "bilabial"
    test_manner = "plosive"

    # testing to see if the parent class's fields were inherited
    def test_consonant_specific_fields(self):
        test_consonant = Consonant(
            symbol = self.test_symbol,
            phonation = self.test_phonation,
            airstream = self.test_airstream,
            place = self.test_place,
            manner = self.test_manner,
        )
        self.assertEqual(
            test_consonant.get_symbol(),
            self.test_symbol
        )
        self.assertEqual(
            test_consonant.get_phonation(),
            self.test_phonation
        )
        self.assertEqual(
            test_consonant.get_airstream(),
            self.test_airstream
        )
        self.assertEqual(
            test_consonant.get_place(),
            self.test_place
        )
        self.assertEqual(
            test_consonant.get_manner(),
            self.test_manner
        )
