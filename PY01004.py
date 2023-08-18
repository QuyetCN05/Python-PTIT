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
        n=int(input())
        k=0
        for i in range(1,n):
            if(gcd(i,n)==1):
                k+=1

        if(nt(k)):
            print('YES')
        else:
            print('NO')
    

