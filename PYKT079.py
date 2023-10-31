from collections import *
from functools import *
from math import *
import io
import os
import sys
import time

if __name__=='__main__':
    for i in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        arr.sort()
        res,ans=arr[0],arr[-1]
        se=set()
        for j in range(res,ans+1): se.add(j)
        cnt=0
        for x in se:
            if x not in arr:
                cnt+=1
        print(cnt)