
from collections import *

if __name__=='__main__':
    for i in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        x=Counter(a)
        for i in x.keys():
            if x[i]%2==1:
                print(i)
        
