from math import *
from collections import *

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
    b=[x for x in a if nt(x)==True]
    res=Counter(b)
    for i in res.keys():
        print(i,res[i],sep=' ')
