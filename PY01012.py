from functools import *
from collections import *
import os,sys,io,time
from math import*

if __name__=='__main__':
    s=input()
    tmp=input()
    p=int(input())
    res = s[ : p-1] + tmp + s[p-1 : ]
    print(res)