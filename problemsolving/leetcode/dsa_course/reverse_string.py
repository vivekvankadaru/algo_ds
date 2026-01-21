'''
Problem Statement (LeetCode – Reverse String)

Given:
A character array s

Task:
Reverse the array in-place.

Constraints:

Do not allocate extra space for another array

Modify the input array directly

🔹 Example
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


def reverseApproach2(s: list) -> list:
    '''
    Docstring for reverseApproach2
    
    :param s: Description
    :type s: list[str]
    :return: Description
    :rtype: list[str]
    This approach uses 2 pointer approach.
    '''
    l=len(s)
    first = 0
    second = l-1
    while first < second:
        t = s[second]
        s[second] = s[first]
        s[first] = t
        first+=1
        second-=1
    return s


def reverseApproach1(s: list) -> list:
    '''
    Docstring for reverseApproach1
    
    :param s: Description
    :type s: list[str]
    :return: Description
    :rtype: list[str]
    This uses list slicing
    '''
    return s[::-1]

def main():
    s=list(input('Enter the string or collection of chars: '))
    print(f'Input string is : {s}')
    s_reverse = reverseApproach2(s)
    print(f'reversed collection of chars: {s_reverse}')
if __name__ == '__main__':
    main()