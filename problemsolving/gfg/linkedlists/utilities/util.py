from dsa.datastructures.single_linked_list import SingleLinkedlist

def generate_linkedlist_from_list(l):
    sl_list=l
    sl=SingleLinkedlist()
    if not sl_list: return sl
    for ele in sl_list:
        sl.append(ele)
    return sl

if __name__=='__main__':
    sl=generate_linkedlist_from_list(None)
    print(sl)
