from collections import *
from functools import *
from math import *
import io, os, sys, time

if __name__=='__main__':
    s=input()
    while len(s) !=1:
        res=len(s)//2
        b=s[:res]
        c=s[res:]
        sum=int(b)+int(c)
        print(sum)
        s=str(sum)

