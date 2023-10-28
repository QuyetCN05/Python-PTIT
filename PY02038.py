from collections import *
from functools import *
from math import *
import io, os, sys, time

if __name__=='__main__':
    sum=0
    n=int(input())
    arr=['']*n
    for i in range(n):
        arr[i]=input()
    c,b=[0]*n,[0]*n
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='C':
                c[i]+=1
                b[j]+=1
    # for i in range(n):
    #     print(c[i],end=' ')
    for i in range(n):
        if c[i]>=2:
            sum+=comb(c[i],2)
    for i in range(n):
        if b[i]>=2:
            sum+=comb(b[i],2)
    print(sum)

                
    
