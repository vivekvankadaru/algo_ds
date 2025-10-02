from dsa.algorithms.merge_sort import merge_sort
import unittest
class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        l = []
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [])

    def test_single_element(self):
        l = [1]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [1])

    def test_sorted_list(self):
        l = [1, 2, 3, 4, 5]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        l = [5, 4, 3, 2, 1]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        l = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_duplicates(self):
        l = [2, 3, 2, 3, 1, 1]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [1, 1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        l = [0, -1, -3, 2, 1]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [-3, -1, 0, 1, 2])

    def test_all_equal(self):
        l = [7, 7, 7, 7]
        merge_sort(l, 0, len(l))
        self.assertEqual(l, [7, 7, 7, 7])

if __name__ == '__main__':
    unittest.main()
