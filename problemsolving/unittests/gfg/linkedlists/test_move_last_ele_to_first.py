from problemsolving.gfg.linkedlists.move_last_ele_to_first import move_last_ele_to_first
from problemsolving.gfg.linkedlists.utilities import util
import unittest

class TestMoveLastEleToFirst(unittest.TestCase):
    def setUp(self):
        self.l1=[1,2,3,4,5]
        self.l2=None
        self.l3=[1]
        self.l4=[1,2]
        self.moved_sl1='5 -> 1 -> 2 -> 3 -> 4 -> None'
        
        self.sl1=util.generate_linkedlist_from_list(self.l1)
        self.sl2=util.generate_linkedlist_from_list(self.l2)
        self.sl3=util.generate_linkedlist_from_list(self.l3)
        self.sl4=util.generate_linkedlist_from_list(self.l4)


    def test_move_last_ele_to_first(self):
        self.assertEqual(self.moved_sl1, str(move_last_ele_to_first(self.sl1)))
        self.assertEqual(str(move_last_ele_to_first(self.sl2)), 'Empty')
        self.assertEqual(str(move_last_ele_to_first(self.sl3)), 'Single Element')
        self.assertEqual(str(move_last_ele_to_first(self.sl4)), '2 -> 1 -> None')


if __name__=='__main__':
    unittest.main()