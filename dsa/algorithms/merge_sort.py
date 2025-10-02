'''
Merge Sort Idea

Divide: Split the array into two halves.

Conquer: Recursively sort each half.

Combine: Merge the two sorted halves into a single sorted array.

'''
def merge(l, p, q, r):
    nl=q-p
    nr=r-q
    l_1sthalf = l[p:q]
    l_2ndhalf = l[q:r]
    i=0
    j=0
    k=p
    while i<nl and j<nr:
        print(f'(i, j, k):{(1, j, k)}')
        print(f'l_1sthalf:{l_1sthalf}, l_2ndhalf:{l_2ndhalf}')
        if l_1sthalf[i] < l_2ndhalf[j]:
            
            print(f'swapping {l_1sthalf[i]} with {l[k]}')
            l[k]=l_1sthalf[i]
            i+=1
            print(f'l:{l}')
        else:
            
            print(f'swapping {l_2ndhalf[j]} with {l[k]}')
            l[k]=l_2ndhalf[j]
            j+=1
            print(f'l:{l}')
        k+=1
    while i<nl and l_1sthalf:
        print(f'i:{i}, nl:{nl}, l_1sthalf:{l_1sthalf}, k:{k}')
        l[k]=l_1sthalf[i]
        i+=1
        k+=1
    while j<nr and l_2ndhalf:
        print(f'j:{j}, nr:{nr}, l_2ndhalf:{l_2ndhalf}, k:{k}')
        l[k]=l_2ndhalf[j]
        j+=1
        k+=1
    print(l)



def merge_sort(l, p, r):
    if p >=r:
        return
    if r-p<=1:
        return l
    q=int((p+r)/2)
    
    merge_sort(l, p, q)
    merge_sort(l, q, r)
    print(f'(p, q, r):{(p, q, r)}')
    merge(l, p, q, r)
    #print(l)
def main():
    l=input('Enter ele to sort sep by ,:').split(',')
    l=list(map(int,l))
    merge_sort(l, 0, len(l))
    print(l)
if __name__=='__main__':
    main()