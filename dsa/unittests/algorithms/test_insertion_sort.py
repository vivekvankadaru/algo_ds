from dsa.algorithms.insertion_sort import insertion_sort, insertion_sort_1

import unittest

class TestInsertionSort(unittest.TestCase):
    
    def test_sorted_list1(self):
        self.assertEqual(insertion_sort_1([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list1(self):
        self.assertEqual(insertion_sort_1([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_list1(self):
        self.assertEqual(insertion_sort_1([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])

    def test_with_duplicates1(self):
        self.assertEqual(insertion_sort_1([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_single_element1(self):
        self.assertEqual(insertion_sort_1([42]), [42])

    def test_empty_list1(self):
        self.assertEqual(insertion_sort_1([]), [])

    def test_negative_numbers1(self):
        self.assertEqual(insertion_sort_1([0, -1, 5, -3, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal_elements1(self):
        self.assertEqual(insertion_sort_1([7, 7, 7, 7]), [7, 7, 7, 7])


    def test_sorted_list(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_list(self):
        self.assertEqual(insertion_sort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        self.assertEqual(insertion_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_single_element(self):
        self.assertEqual(insertion_sort([42]), [42])

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(insertion_sort([0, -1, 5, -3, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal_elements(self):
        self.assertEqual(insertion_sort([7, 7, 7, 7]), [7, 7, 7, 7])


if __name__=='__main__':
    unittest.main()