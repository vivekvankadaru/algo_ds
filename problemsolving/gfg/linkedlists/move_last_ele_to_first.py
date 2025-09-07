'''
Given a singly linked list. The task is to move the last node to the front in a given List.
Input: 2->5->6->2->1
Output: 1->2->5->6->2
Explanation : Node 1 moved to front.
Input: 1->2->3->4->5
Output: 5->1->2->3->4
Explanation : Node 5 moved to front.
'''

from dsa.datastructures.single_linked_list import SingleLinkedlist
from problemsolving.gfg.linkedlists.utilities import util
import sys
print(sys.path)
def move_last_ele_to_first(sl):
    curr=sl.head
    prev=sl.head
    while curr:
        if curr.next is None:
            pass
        prev=curr
        curr=curr.next
def main():
    str_sl=input('enter the ele of linked list sep by ,:')
    sl=util.generate_linkedlist_from_list(str_sl.split(','))

    sl = move_last_ele_to_first(sl)
    print(sl)
if __name__=='__main__':
    main()