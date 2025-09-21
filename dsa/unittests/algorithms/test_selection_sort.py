from dsa.algorithms.selection_sort import selection_sort

import unittest

class TestInsertionSort(unittest.TestCase):
    
    def test_sorted_list(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_list(self):
        self.assertEqual(selection_sort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        self.assertEqual(selection_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_single_element(self):
        self.assertEqual(selection_sort([42]), [42])

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(selection_sort([0, -1, 5, -3, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal_elements(self):
        self.assertEqual(selection_sort([7, 7, 7, 7]), [7, 7, 7, 7])


if __name__=='__main__':
    unittest.main()