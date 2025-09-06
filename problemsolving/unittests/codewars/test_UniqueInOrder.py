from problemsolving.codewars import UniqueInOrder
import unittest

class TestUniqueInOrder(unittest.TestCase):
    def setUp(self):
        self.s='AAAABBBCCDAABBB'

    def test_convert_str_to_arr_repeating(self):
        arr=['AAAA','BBB','CC','D','AA','BBB']
        self.assertEqual(arr, UniqueInOrder.convert_str_to_arr_repeating(self.s))


if __name__ == '__main__':
    unittest.main()