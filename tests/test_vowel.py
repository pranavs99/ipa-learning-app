import unittest

from ipa_learning_app.vowel import Vowel


class TestVowelClass(unittest.TestCase):
    test_symbol = "i"
    test_height = "high"
    test_backness = "front"
    test_rounding = "unrounded"

    # should be consonant in all Vowel objects
    vowel_phonation = "voiced"
    vowel_airstream = "pulmonic"

    # testing to see if the parent class's fields were inherited
    def test_vowel_specific_fields(self):
        test_vowel = Vowel(
            symbol = self.test_symbol,
            height = self.test_height,
            backness = self.test_backness,
            rounding = self.test_rounding
        )
        self.assertEqual(
            test_vowel.get_symbol(),
            self.test_symbol
        )
        self.assertEqual(
            test_vowel.get_phonation(),
            self.vowel_phonation
        )
        self.assertEqual(
            test_vowel.get_airstream(),
            self.vowel_airstream
        )
        self.assertEqual(
            test_vowel.get_height(),
            self.test_height
        )
        self.assertEqual(
            test_vowel.get_backness(),
            self.test_backness
        )
        self.assertEqual(
            test_vowel.get_rounding(),
            self.test_rounding
        )