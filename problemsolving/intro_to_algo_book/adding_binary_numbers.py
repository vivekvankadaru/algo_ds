'''
adding 2 binary numbers

'''

def validate_binary(i):
    
    if not i: return is_binary
    l=list(i)
    l1=list(map(lambda x: x in ['0', '1'], l))
    return all(l1)

def sum_of_binary(a, b):
    carry = 0
    result = []

    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    for i in range(max_len - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        result.append(str(total % 2))
        carry = total // 2

    if carry:
        result.append('1')

    result_str = ''.join(result[::-1])

    if len(result_str) > max_len:
        return result_str

    if set(result_str) == {'0'}:
        return '0' * max_len

    return result_str.zfill(max_len)
def main():
    a=input('Enter 1st binary number:')
    b=input('Enter 2nd binary number:')
    is_bin_a=validate_binary(a)
    is_bin_b=validate_binary(b)
    while not (is_bin_a and is_bin_b):
            print('Any of a:{a}, b:{b} is non binary.Enter again')
            a=input('Enter 1st binary number:')
            b=input('Enter 2nd binary number:')
            is_bin_a=validate_binary(a)
            is_bin_b=validate_binary(b)
    #a=int(a)
    #b=int(b)
    c=sum_of_binary(a,b)
    print(c)
    
if __name__ == '__main__':
    main()