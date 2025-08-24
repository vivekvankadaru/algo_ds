'''
Write a function named first_non_repeating_letter† that takes a string input,
 and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. 
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, 
it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter
 for historical reasons, but your function should handle any Unicode character.

'''

from collections import Counter
def first_non_repeating_letter(s):
    lower_s = s.lower()
    counts_of_letters = Counter(lower_s)
    found_nonrepetitive=False
    for c in s:
        if counts_of_letters[c.lower()]==1:
            found_nonrepetitive=True
            return c
    if not found_nonrepetitive:
        return ''
if __name__ == '__main__':
    s=input('Enter the string:')
