'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 
'''

def TargetFinder3(l: list, target: int):
    '''
    Docstring for TargetFinder3
    
    :param l: Description
    :type l: list
    :param target: Description
    :type target: int
    This approach uses hashing and the time complexity is O(n)

    '''
    d={}
    for i, ele in enumerate(l):
        other_ele = target - ele
        if other_ele in d:
            return [d[other_ele], i]
        else:
            d[ele] = i
    print(d)
    return 'Nothing found'
def TargetFinder2(l: list, target: int):
    '''
    Docstring for TargetFinder2
    
    :param l: Description
    :type l: list
    :param target: Description
    :type target: int
    2 POINTER technique
    This is not a feasible solution as the input list needs to be sorted and sorting changes the 
    indexes.
    Time complexity - O(nlogn)
    '''
    from copy import deepcopy
    l_copy = deepcopy(l)
    l.sort()
    l1=len(l)
    i=0
    j=l1-1
    while i < l1 and j > 0:
        if l[i] + l[j] > target:
            j-=1
        elif l[i] + l[j] < target:
            i+=1
        else:
            index_i = l_copy.index(l[i])
            
            index_j = l_copy.index(l[j])
            if index_i==index_j:
                print('There are dups')
                l_copy.pop(index_i)
                index_j = l_copy.index(l[j])
                index_j+=1
            print(f'Target found at indexes {index_i}, {index_j}: ele - {l[i]}, {l[j]}')
            return True
    print('Not found satisfying the criteria')
    return False
    

def TargetFinder1(l: list, target: int):
    '''
    Docstring for TargetFinder1
    
    :param l: Description
    :type l: list
    :param target: Description
    :type target: int
    Time complexity - O(n**2)
    
    '''
    l1=len(l)
    for i in range(l1):
        for j in range(i+1, l1):
            if l[i]+l[j]==target:
                print(f'Target found at indexes {i}, {j}: ele - {l[i]}, {l[j]}')
                return True
    print('Not found satisfying the criteria')
    return False
        
    
def main():
    l=list(map(int, input('Enter the integers sep by ,: ').split(',')))
    target = int(input('Enter the target: '))
    print(f'input l: {l}, target: {target}')
    found_target = TargetFinder3(l, target)
    print(f'{found_target}')
if __name__=='__main__':
    main()