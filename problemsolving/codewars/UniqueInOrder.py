'''
Description:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
'''


def convert_str_to_arr_repeating(s):
    l=[]
    current=0
    prev=0
    ele_arr=s[current]
    #l.append(ele_arr)
    for i in range(len(s)):
        if s[current] == s[prev]:
            current+=1
        else:
            l.append(ele_arr)
            ele_arr=s[current]
            #temp=prev
            prev=current
            
            current+=1
    l.append(ele_arr)
    return l
            

def unique_in_order(s):
    if not s: return []
    arr=convert_str_to_arr_repeating(s)
    #arr=[ele[0] for ele in arr]
    
    return arr

def main():
    s=input('Enter the string or enter array sep by ,:')
    if ',' in s:
        s=s.split(',')
    uniqueinorder = unique_in_order(s)
    print(uniqueinorder)
if __name__ == '__main__':
    main()