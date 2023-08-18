from math import *

def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True

if __name__=='__main__':
    t=int(input())
    while t !=0:
        t-=1
        s=input()
        str=''
        a=list(s)
        for i in range(len(a)-4,len(a)):
            str+=a[i]
        if(nt(int(str))):
            print('YES')
        else:
            print('NO')
