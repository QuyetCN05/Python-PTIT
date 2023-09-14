from collections import *

if __name__=='__main__':
    n=int(input())
    res=set()
    for i in range(n):
        s=input()
        res.add(s)
    
    print(len(res))
