'''
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

We start with the second element of the array as the first element is assumed to be sorted.
Compare the second element with the first element if the second element is smaller then swap them.
Move to the third element, compare it with the first two elements, and put it in its correct position
Repeat until the entire array is sorted.

'''

def main():
    l=input('Enter the numbers to sort sep by ,:').split(',')
    a=1 if l else 2
    print(a)
    l=list(map(int, l)) if l else []
    print(l)

if __name__ == '__main__':
    main()