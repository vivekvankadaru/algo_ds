'''
Docstring for problemsolving.leetcode.dsa_course.squares_of_sorted_array
Problem Statement (LeetCode – Squares of a Sorted Array)

Given:
An integer array nums sorted in non-decreasing order (may contain negative numbers)

Task:
Return an array of the squares of each number, also sorted in non-decreasing order.

🔹 Example
Input:  nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Input:  nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

'''

def SquaresOfSortedArrayApproach3(l):
    '''
    Docstring for SquaresOfSortedArrayApproach3
    
    :param l: Description
    this is optimal approach given in online and chatgpt

    '''

    n = len(l)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        if abs(l[left]) > abs(l[right]):
            result[pos] = l[left] ** 2
            left += 1
        else:
            result[pos] = l[right] ** 2
            right -= 1
        pos -= 1

    return result


def SquaresOfSortedArrayApproach2(l):
    '''
    Docstring for SquaresOfSortedArrayApproach2
    
    :param l: Description
    This approach is mine.
    1) first find the first non -ve number in the list.
    2) split the list into 2. first part is of -ve numbers, 2nd part is of non -ve numbers.
    3) compare 2nd part element wise with first part element wise in reverse. (as first part is -ve)
    4) append the values to a new array based on comparision.
    5) if any of the lists exhausted, copy the remaining elements of lists to the new array.

    Some complicated approach but only advantage is NO comparision of all elements.
    '''
    i = 0
    len_l = len(l)
    for e in range(len_l):
        if l[e] >= 0:
            j = e
            break
    l1 = l[i:j]
    l2 = l[j:len_l]
    #l1 = l1[::-1] # sorted reverse since -ve numbers
    new_array = []
    k = len(l1)-1
    m = 0
    while k >= 0 and m < len(l2):
        if l1[k]**2 > l2[m]**2:
            new_array.append(l2[m]**2)
            m+=1
        else:
            new_array.append(l1[k]**2)
            k-=1
    while m < len(l2):
        new_array.append(l2[m]**2)
        m+=1
    while k >= 0:
        new_array.append(l1[k]**2)
        k-=1
    print(f'new_array: {new_array}')
    return new_array


def SquaresOfSortedArrayApproach1(l):
    #naive solution
    return [ele**2 for ele in l].sort()
def main():
    l=list(map(int, input('Enter the integers sep by ,: ').split(',')))
    squares=SquaresOfSortedArrayApproach2(l)
    print(f'Squares of sorted array: {squares}')
if __name__ == '__main__':
    main()