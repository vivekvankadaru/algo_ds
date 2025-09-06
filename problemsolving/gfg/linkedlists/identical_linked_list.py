'''
Given two singly linked lists. The task is to determine if the two linked lists are identical or not.
 Two linked lists are considered identical if
  
    they contain the same data in the same order.
   If the linked lists are identical, return true otherwise, return false.

   Input: LinkedList1: 1->2->3->4->5->6, LinkedList2: 99->59->42->20
Output: false

Input: LinkedList1: 1->2->3->4->5,
 LinkedList2: 1->2->3->4->5
Output: true

'''
    
import sys
from dsa.datastructures import single_linked_list
import logging

#logging.basicConfig()
log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
#print(sys.path)
handler=logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s:%(message)s'))
log.addHandler(handler)
log.info('Hi')


def is_identical(l1, l2):
    return l1==l2

def generate_linked_list(l):
    sl=single_linked_list.SingleLinkedlist()
    for i in l:
        sl.append(i)
    return sl

def main():
    str_l = input('Enter the linked list elements followed by ,:')
    str_l1 = input('Enter the linked list elements followed by ,:')
    l=generate_linked_list(str_l.split(','))
    l1=generate_linked_list(str_l1.split(','))

    is_linkedlists_identical = is_identical(l, l1)
    if is_linkedlists_identical:
        log.info(f'Both {l} and {l1} are identical')
    else:
        log.info(f'{l} and {l1} are not identical')

if __name__=='__main__':
    main()