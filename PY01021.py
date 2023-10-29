from collections import *
from functools import *
from math import *
import io, os, sys, time

if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        a=list(s)
        b=[x for x in a if x.isalpha()]
        c=[int(x) for x in a if x.isdigit()]
        b.sort()
        for j in b:
            print(j,end='',sep=' ')
        print(sum(c))
        