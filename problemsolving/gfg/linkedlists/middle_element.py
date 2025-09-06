'''
Middle Node in a Linked List
Given the head of singly linked list, find middle node of the linked list.

If the number of nodes is odd, return the middle node.
If the number of nodes is even, there are two middle nodes, so return the second middle node.

1->2->3->4->5
return 3

10->20->30->40->50->60
40 (second middle node)

'''

#custom
from problemsolving.gfg.linkedlists.utilities import util

#stdlib
import logging
log=logging.getLogger(__name__)
loghandler=logging.StreamHandler()
log.addHandler(loghandler)
log.setLevel(logging.INFO)


def fetch_middle_element(sl):
    len_sl=len(sl)
    #mid_index = int(len_sl/2)
    mid_index = int(len_sl/2)+1
    '''
    if len_sl%2==0: #even
        mid_index=mid_index+1
    else: #odd
        mid_index=mid_index+1
    '''
    return sl.fetchElementFromIndex(mid_index)

def main():
    l=input('Enter the elements of linked list sep by ,:')
    sl=util.generate_linkedlist_from_list(l)

    middle_ele = fetch_middle_element(sl)
    print(f'The middile element is {middle_ele}')


if __name__=='__main__':
    main()