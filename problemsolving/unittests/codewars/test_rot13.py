import unittest
from problemsolving.codewars.rot13 import rot13

class TestRot13(unittest.TestCase):
    def test_basic_lowercase(self):
        self.assertEqual(rot13('abc'), 'nop')
        self.assertEqual(rot13('nop'), 'abc')
        self.assertEqual(rot13('abcdefghijklmnopqrstuvwxyz'), 'nopqrstuvwxyzabcdefghijklm')

    def test_basic_uppercase(self):
        self.assertEqual(rot13('ABC'), 'NOP')
        self.assertEqual(rot13('NOP'), 'ABC')
        self.assertEqual(rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'NOPQRSTUVWXYZABCDEFGHIJKLM')

    def test_mixed_case(self):
        self.assertEqual(rot13('AbcNop'), 'NopAbc')
        self.assertEqual(rot13('HelloWorld'), 'UryybJbeyq')

    def test_numbers_and_symbols(self):
        self.assertEqual(rot13('123!@#'), '123!@#')
        self.assertEqual(rot13('abc123'), 'nop123')
        self.assertEqual(rot13('ABC!@#'), 'NOP!@#')

    def test_empty_string(self):
        self.assertEqual(rot13(''), '')

    def test_non_alpha(self):
        self.assertEqual(rot13('!@#$%^&*()'), '!@#$%^&*()')

if __name__ == '__main__':
    unittest.main()