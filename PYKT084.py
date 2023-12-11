from collections import *
from functools import *
from math import *
import io,os,sys,time

if __name__=='__main__':
    n = int(input())
    a = []
    for i in range(n): a.append(input())
    # for x in a:
    #     print(x)
    res, tmp = [], []
    for i in range(n):
        if len(a[i].split()): tmp.append(a[i])
        else:
            res.append(tmp)
            tmp = []
    if len(tmp) > 0: res.append(tmp)
    for x in res: print(x[0], len(x) - 1, sep = ': ')
        


