from functools import *
from collections import *
import os,sys,io,time
from math import *


if __name__=='__main__':
    for i in range(int(input())):
        n,b=map(int,input().split())
        s=''
        while n >0:
            res=n%b
            if res <10:
                s=str(res)+s
            else:
                s=chr(ord('A')+res-10)+s
            n //=b
        print(s)