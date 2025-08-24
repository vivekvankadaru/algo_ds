import unittest
from problemsolving.codewars.first_non_repeating_letter import first_non_repeating_letter

class TestFirstNonRepeatingLetter(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter('aabbccdde'), 'e')
        self.assertEqual(first_non_repeating_letter('a'), 'a')
        self.assertEqual(first_non_repeating_letter(''), '')

    def test_all_repeating(self):
        self.assertEqual(first_non_repeating_letter('aabbcc'), '')
        self.assertEqual(first_non_repeating_letter('SSss'), '')

    def test_unicode(self):
        self.assertEqual(first_non_repeating_letter('åäöåäöx'), 'x')
        self.assertEqual(first_non_repeating_letter('ßßa'), 'a')

    def test_case_sensitivity(self):
        self.assertEqual(first_non_repeating_letter('AaBbCcD'), 'D')
        self.assertEqual(first_non_repeating_letter('aAbBcCdD'), '')

    def test_numbers_and_symbols(self):
        self.assertEqual(first_non_repeating_letter('112233!'), '!')
        self.assertEqual(first_non_repeating_letter('!!@@##$'), '$')
        self.assertEqual(first_non_repeating_letter('112233'), '')

if __name__ == '__main__':
    unittest.main()