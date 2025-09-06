from problemsolving.codewars import codewars_10_min_walk

import unittest

class Test10MinWalk(unittest.TestCase):
    def setUp(self):
        self.arr1=['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's']
        self.arr2=['e', 'e', 'w', 'w', 'e', 'w', 'w', 'e', 'e', 'w']
    def test_ReachedToSamePoint(self):
        self.assertEqual(True, codewars_10_min_walk.ReachedToSamePoint(self.arr1))
        self.assertEqual(True, codewars_10_min_walk.ReachedToSamePoint(self.arr2))
        
if __name__ == '__main__':
    unittest.main()
