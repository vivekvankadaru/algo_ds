'''
ROT13 is a simple letter substitution cipher that 
replaces a letter with the letter 13 letters after 
it in the alphabet. ROT13 is an example of the
 Caesar cipher.

Create a function that takes a string and returns 
the string ciphered with Rot13. If there are numbers 
or special characters included in the string, they 
should be returned as they are. Only letters from
 the latin/english alphabet should be shifted, like 
 in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''
ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
DICT_NUM_ALPHABETS={}
DICT_ALPHA_NUM={}
for i,c in enumerate(ALPHABETS):
    DICT_NUM_ALPHABETS[i]=c
    DICT_ALPHA_NUM[c]=i 

def generate_index(c):
    i=DICT_ALPHA_NUM.get(c,None)
    if i is None:
        return
    if i+13<=25:
        return i+13
    else:
        return i-13
def rot13(s):
    rot13_s=''
    #s=s.lower()
    for c in s:
        if c.islower():
            n=generate_index(c)
            new_c=DICT_NUM_ALPHABETS.get(n, None)
            if new_c is None:
                new_c = c
        else:
            n=generate_index(c.lower())
            new_c=DICT_NUM_ALPHABETS.get(n,None)
            if new_c is None:
                new_c = c
            else:
                new_c=new_c.upper()
        rot13_s+=new_c
    return rot13_s

if __name__ == '__main__':
    s=input('Enter string to cipher using ROT13:')
    print(rot13(s))