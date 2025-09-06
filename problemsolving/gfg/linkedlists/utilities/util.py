from dsa.datastructures.single_linked_list import SingleLinkedlist

def generate_linkedlist_from_list(l):
    sl_list=l
    sl=SingleLinkedlist()
    for ele in sl_list:
        sl.append(ele)
    return sl
