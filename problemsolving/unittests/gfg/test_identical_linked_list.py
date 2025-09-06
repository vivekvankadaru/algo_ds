from problemsolving.gfg import identical_linked_list
from dsa.datastructures.single_linked_list import SingleLinkedlist
import unittest

class Testidentical_linked_list(unittest.TestCase):
    
    def setUp(self):
        self.ll = SingleLinkedlist()
        self.l2 = SingleLinkedlist()


    def test_generate_linked_list(self):
        l=[1,2,3,4,5]
        l1=SingleLinkedlist()
        l1.append(1)
        l1.append(2)
        l1.append(3)
        l1.append(4)
        l1.append(5)
        new_l=identical_linked_list.generate_linked_list(l)
        print(f'new_l:{new_l}')
        print(l1)
        self.assertEqual(new_l, l1)


if __name__ == '__main__':
    unittest.main()