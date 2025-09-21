'''
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

We start with the second element of the array as the first element is assumed to be sorted.
Compare the second element with the first element if the second element is smaller then swap them.
Move to the third element, compare it with the first two elements, and put it in its correct position
Repeat until the entire array is sorted.

'''

def insertion_sort_1(l):
    if not l: return []
    n=len(l)
    if n==1: return l

    for i in range(1,n):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    return l 

def insertion_sort(l):
    #l=[5,3,4,1,2]
    if not l: return []
    l1=[]
    l1.append(l[0])
    len_l=len(l)
    for i in range(1,len(l)):
        j=0
        while j<len(l1) and l[i]>l1[j]:
        
            j+=1
        l1.insert(j, l[i])
        print(f'{i}th iteration: {l1}')
    return l1
def main():
    l=input('Enter the numbers to sort sep by ,:')
    while not l:
        print('Input not entered')
        l=input('Enter the numbers to sort sep by ,:')
    if l:
        l=l.split(',')
        l=list(map(int, l))
    #print(l)
    sorted_l = insertion_sort_1(l)
    print(sorted_l)

if __name__ == '__main__':
    main()