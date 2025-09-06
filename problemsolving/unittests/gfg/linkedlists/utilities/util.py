from problemsolving.gfg.linkedlists.utilities import util
import unittest

class TestUtilTesting(unittest.TestCase):
    
    def test_generate_linkedlist_from_list(self):
        l=[1,2,3,4,5]
        sl=util.generate_linkedlist_from_list(l)
        str_sl='1->2->3->4->5->None'
        self.assertEqual(str_sl,str(sl))

if __name__ == '__main__':
    unittest.main()