from problemsolving.intro_to_algo_book.adding_binary_numbers import sum_of_binary
import unittest
class TestSumOfBinary(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(sum_of_binary('0', '0'), '0')
        self.assertEqual(sum_of_binary('1', '0'), '1')
        self.assertEqual(sum_of_binary('0', '1'), '1')
        self.assertEqual(sum_of_binary('1', '1'), '10')

    def test_carry_over(self):
        self.assertEqual(sum_of_binary('11', '01'), '100')
        self.assertEqual(sum_of_binary('101', '111'), '1100')
        self.assertEqual(sum_of_binary('111', '111'), '1110')

    def test_longer_numbers(self):
        self.assertEqual(sum_of_binary('10101', '11011'), '110000')
        self.assertEqual(sum_of_binary('11111', '11111'), '111110')

    def test_with_leading_zeros(self):
        self.assertEqual(sum_of_binary('001', '001'), '010')
        self.assertEqual(sum_of_binary('0000', '0000'), '0000')

    def test_all_zeros(self):
        self.assertEqual(sum_of_binary('000', '000'), '000')

if __name__=='__main__':
    unittest.main()