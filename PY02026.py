from math import *
from collections import *
from functools import *


if __name__=='__main__':
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    set_1=set(a)
    set_2=set(b)
    if set_1==set_2:
        print('YES')
    else:
        print('NO')