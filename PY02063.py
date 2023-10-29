from collections import *
from functools import *
from math import *
import io
import os
import sys
import time

if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    c,d,e,f=arr[:2],arr[:3],arr[-3:],arr[-2:]
    x,y,z,t=1,1,1,1
    for i in c:
        x*=i
    for i in d:
        y*=i
    for i in e:
        z*=i
    for i in f:
        t*=i
    print(max(x,y,z,t,x*arr[-1]))