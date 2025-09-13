from problemsolving.gfg.linkedlists import delete_alternate_nodes
from problemsolving.gfg.linkedlists.utilities import util
import unittest

class TestDeleteAlternateNodes(unittest.TestCase):
    def setUp(self):
        l=[1,2,3,4,5]
        self.sl=util.generate_linkedlist_from_list(l)
        l1=[1,2,3]
        self.sl1=util.generate_linkedlist_from_list(l1)
        l2=[1]
        self.sl2=util.generate_linkedlist_from_list(l2)

    def test_delete_alternate(self):
        self.assertEqual(str(delete_alternate_nodes.delete_alternate_nodes(self.sl)), '1->3->5->None')
        self.assertEqual(str(delete_alternate_nodes.delete_alternate_nodes(self.sl1)), '1->3->None')
        self.assertEqual(str(delete_alternate_nodes.delete_alternate_nodes(self.sl2)), '1->None')

if __name__=='__main':
    unittest.main()