from collections import *
from functools import *
from math import *
import os,io,sys,time



a,arr=[0]*101,[]


def show(n):
    arr.append(a[1:n+1])

def Try(i,n):
    for j in range(0,2):
        a[i]=j
        if i==n:show(n)
        else: Try(i+1,n)

if __name__=='__main__':
    n=int(input())
    Try(1,n)
    for x in arr:
        print(x)

