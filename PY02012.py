from collections import *
from functools import *
from math import *
import os,io,sys,time




if __name__=='__main__':
    n=int(input())
    arr=[]
    while True:
        tmp=list(map(int,input().split()))
        arr+=tmp
        if len(arr)==n: break
    chan=[x for x in arr if x%2==0]
    le=[x for x in arr if x%2==1]
    le.sort()
    chan.sort(reverse=True)
    mark=[0]*n
    for i in range(n):
        if arr[i]%2==1: mark[i]=1
    for i in range(n):
        if mark[i]:
            print(le[-1],end=' ')
            le.pop()
        else:
            print(chan[-1],end=' ')
            chan.pop()
