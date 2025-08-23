import unittest
import sys
print(f'sys.path: {sys.path}')
from dsa.datastructures.single_linked_list import SingleLinkedlist, Node

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = SingleLinkedlist()

    def test_append_and_repr(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(str(self.ll), "1->2->3->None")

    def test_insert_at_beginning(self):
        self.ll.append(1)
        self.ll.InsertAtBeginning(0)
        self.assertEqual(str(self.ll), "0->1->None")

    def test_insert_after(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.insertAfter(3, 2)
        self.assertEqual(str(self.ll), "1->2->3->None")
        # Insert after non-existent value
        self.ll.insertAfter(4, 99)
        self.assertEqual(str(self.ll), "1->2->3->None")

    def test_insert_at_index(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.InsertAtIndex(1, 5)
        self.assertEqual(str(self.ll), "1->5->2->None")
        # Insert at beginning
        self.ll.InsertAtIndex(0, 0)
        self.assertEqual(str(self.ll), "0->1->5->2->None")
        # Insert at out-of-bounds index
        self.ll.InsertAtIndex(10, 99)
        self.assertNotIn("99", str(self.ll))

    def test_delete_at_beginning(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.deleteAtBeginning()
        self.assertEqual(str(self.ll), "2->None")
        # Delete when list is empty
        self.ll.deleteAtBeginning()
        self.ll.deleteAtBeginning()
        self.assertEqual(str(self.ll), "None -> None Empty linked list")

    def test_delete_node_value(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(1)
        self.ll.deleteNodeValue(1)
        self.assertEqual(str(self.ll), "2->None")
        # Delete non-existent value
        self.ll.deleteNodeValue(99)
        self.assertEqual(str(self.ll), "2->None")

    def test_delete_node_at_index(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.deleteNodeAtIndex(1)
        self.assertEqual(str(self.ll), "1->3->None")
        # Delete at out-of-bounds index
        result = self.ll.deleteNodeAtIndex(10)
        self.assertEqual(result, 'Index value is higher than length')

    def test_search(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        with self.assertLogs() as log:
            self.ll.search(2)
        self.assertIn('2 found', log.output[0])
        with self.assertLogs() as log:
            self.ll.search(99)
        self.assertIn('No 99 found', log.output[0])

    def test_len(self):
        self.assertEqual(len(self.ll), 0)
        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(len(self.ll), 2)

    def test_repr_empty(self):
        self.assertEqual(str(self.ll), "None -> None Empty linked list")

if __name__ == '__main__':
    unittest.main()