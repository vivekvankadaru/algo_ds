'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

from collections import Counter

def scramble(s1, s2):
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    for char, needed in count_s2.items():
        if count_s1[char] < needed:
            return False
    return True
            


def main():
    str1,str2=input('Enter strs sep by ,').split(',')

    print(scramble(str1, str2))

if __name__ == '__main__':
    main()