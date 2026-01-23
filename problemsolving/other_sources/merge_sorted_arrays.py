'''
Docstring for problemsolving.other_sources.merge_sorted_arrays
Problem Statement — Merge Sorted Array

Given:

Two integer arrays:

nums1 of size m + n

First m elements are sorted

Last n elements are empty (0 placeholders)

nums2 of size n, sorted

Integers m and n

Task:
Merge nums2 into nums1 as one sorted array, in-place.

🔹 Example 1
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output:
[1,2,2,3,5,6]

🔹 Example 2
Input:
nums1 = [1], m = 1
nums2 = [],  n = 0

Output:
[1]

'''

def merge_sorted_arrays(a1:list, a2:list):
    l2 = len(a2)
    l1 = len(a1) - l2
    
    i, j = 0, 0
    while  j < l2:
        if a1[i] < a2[j]:
            if i < l1+j:
                i+=1
            else:
                a1[i] = a2[j]
                i+=1
                j+=1
        else:
            t=a1[i]
            
            a1[i] = a2[j]
            a1.insert(i, t)
            a1.pop()
            i+=1
            j+=1
    return a1

def main():
    arr2 = list(map(int, input('Enter the sorted array 2 of ele sep by ,: ').split(',')))
    arr1 = list(map(int, input('Enter the sorted array 1 of ele sep by ,: ').split(','))) + [0]*len(arr2)
    
    merged_array = merge_sorted_arrays(arr1, arr2)
    print(f'merged array is : {merged_array}')
if __name__ == '__main__':
    main()