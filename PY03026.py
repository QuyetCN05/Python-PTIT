
from math import *

def nt(n):
    if n<2:
        return False
    
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True

if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if gcd(a[i],a[j])==1:
                print(a[i],a[j])
   