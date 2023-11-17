from collections import *
from functools import *
from math import *
import io
import os
import sys
import time


if __name__=='__main__':
    n=int(input())
    arr=[]
    while True:
        try:
            s=input().split()
            for j in s:
                arr.append(int(j))
        except EOFError:
            break
    while True:
        try:
            s = input().split()
            for x in s: arr.append(int(x))
        except EOFError: break
    # arr.sort()
    se,ma=set(),arr[-1]
    check=0
    for x in arr:
        se.add(x)
    for x in range(1,ma+1):
        if x not in se:
            print(x)
            check=1
    if check==0:
        print('Excellent!')


# if __name__ == '__main__':
#     n = int(input())
#     a = []
#     while True:
#         try:
#             s = input().split()
#             for x in s: a.append(int(x))
#         except EOFError: break
#     check = 0
#     s, ma = set(), a[-1]
#     for x in a: s.add(x)
#     for x in range(1, ma + 1):
#         if x not in s:
#             print(x)
#             check = 1
#     if not check: print('Excellent!')
        
