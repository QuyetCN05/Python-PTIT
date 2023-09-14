from math import *

def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        str=s[0:3]
        tmp=s[-3]+s[-2]+s[-1]
        if(nt(int(str)) and nt(int(tmp))):
            print('YES')
        else:
            print('NO')
       
