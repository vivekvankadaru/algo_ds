'''
The rgb function is incomplete. Complete it so that
 passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
'''

def convert_to_hex(l):
    hex_l=[]
    for ele in l:
        if ele > 255:
            ele=255
        hex_ele = hex(ele)
        str_hex_ele=str(hex_ele)
        if len(str_hex_ele)==1:
            str_hex_ele='0'+str_hex_ele
        hex_l.append(str_hex_ele)

    return ''.join(hex_l)

def main():
    inp=input('Enter the input sep by ,:')
    inp_l=inp.split(',')
    l=[]
    for ele in inp_l:
        l.append(int(ele))
    
    hex_d=convert_to_hex(l)
    print(hex_d)
if __name__ == '__main__':
    main()