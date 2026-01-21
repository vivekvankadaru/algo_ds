from problemsolving.leetcode.dsa_course.reverse_string import reverseApproach2, reverseApproach1
import unittest

class TestReverseString(unittest.TestCase):
    
    def test_reverse_hello(self):
        s = ["h", "e", "l", "l", "o"]
        self.assertEqual(reverseApproach2(s), ["o", "l", "l", "e", "h"])
    
    def test_reverse_hannah(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.assertEqual(reverseApproach2(s), ["h", "a", "n", "n", "a", "H"])
    
    def test_single_character(self):
        s = ["a"]
        self.assertEqual(reverseApproach2(s), ["a"])
    
    def test_two_characters(self):
        s = ["a", "b"]
        self.assertEqual(reverseApproach2(s), ["b", "a"])
    
    def test_empty_string(self):
        s = []
        self.assertEqual(reverseApproach2(s), [])
    
    def test_palindrome(self):
        s = ["r", "a", "c", "e", "c", "a", "r"]
        self.assertEqual(reverseApproach2(s), ["r", "a", "c", "e", "c", "a", "r"])
    
    def test_approach1_hello(self):
        s = ["h", "e", "l", "l", "o"]
        self.assertEqual(reverseApproach1(s), ["o", "l", "l", "e", "h"])
    
    def test_approach1_hannah(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.assertEqual(reverseApproach1(s), ["h", "a", "n", "n", "a", "H"])


if __name__ == '__main__':
    unittest.main()

