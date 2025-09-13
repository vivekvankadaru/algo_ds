'''
Given a Singly Linked List, starting from the second
 node delete all alternate nodes of it. For example,
   if the given linked list is 1->2->3->4->5 then
     your function should convert it to 1->3->5, 
     and if the given linked list is 1->2->3->4 
     then convert it to 1->3.
 
'''

from problemsolving.gfg.linkedlists.utilities import util
from dsa.datastructures.single_linked_list import SingleLinkedlist

def delete_alternate_nodes(sl):
    curr=sl.head
    if not curr:
        return 'linked list {sl} is empty'
    
    prev=sl.head
    consider=True
    while curr:
        if consider:
            prev=curr
        else:
            t=curr.next
            prev.next=t
            prev=curr.next
        consider=not consider
        
        curr=curr.next
    return sl


def main():
    l_sl=input('Enter the ele in linked list sep by ,')
    l_sl=l_sl.split(',')
    sl_l=util.generate_linkedlist_from_list(l_sl)
    sl=delete_alternate_nodes(sl_l)
    print(sl)
if __name__=='__main__':
    main()