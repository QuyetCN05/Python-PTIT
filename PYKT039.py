from functools import *
from collections import *
import os,sys,io,time
from math import*


if __name__=='__main__':
    for i in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        brr=list(map(int,input().split()))
        arr.sort(),brr.sort()
        cnt=0
        for i in range(n):
            if arr[i] > brr[i]: cnt+=1
        if cnt ==0:
            print('YES')
        else:
            print('NO')
