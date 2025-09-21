'''
Consider sorting n numbers stored in array A[1:n] by 
finding smallest of A[1:n] and exchanginh with A[1]
Then find the smallest element of A[2:n] and exchange
it with A[2]. Then find the smallest element of A[3:n] and exchange
it with A[3]. Continue this manner for the 1st n-1 elements of A
This is known as selection sort.

'''

def selection_sort(l):
    n=len(l)
    #start_index=0
    for i in range(n):
        small_ele=l[i]
        ind=0
        ind_modified=False
        for j in range(i+1,n):
            if l[j]<small_ele:
                small_ele=l[j]
                ind=j
                ind_modified=True
            #print(l)
        
        if ind_modified:
            t=l[i]
            l[i]=small_ele
            l[ind]=t
        
    return l
def main():
    l=input('Enter the ele to sort sep by ,:').split(',')
    l=list(map(int,l))
    l=selection_sort(l)
    print(l)
if __name__=='__main__':
    main()