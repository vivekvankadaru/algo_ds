from problemsolving.gfg.linkedlists import middle_element
from dsa.datastructures.single_linked_list import SingleLinkedlist
from problemsolving.gfg.linkedlists.utilities import util

import unittest
class TestMiddleElement(unittest.TestCase):
    def setUp(self):
        self.sl=SingleLinkedlist()
        self.sl1=SingleLinkedlist()
        l1=[1,2,3,4,5]
        l2=[1,2,3,4,5,6,7,8,9,10]

        for ele in l1:
            self.sl.append(ele)

        for ele in l2:
            self.sl1.append(ele)
    
    def test_fetch_middle_element(self):
        self.assertEqual(3, middle_element.fetch_middle_element(self.sl))
        self.assertEqual(6, middle_element.fetch_middle_element(self.sl1))
        
if __name__ == '__main__':
    unittest.main()
