from collections import *
from functools import *
from math import *
import io
import os
import sys
import time


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n): arr[i] = list(map(int, input().split()))
    s = set()
    if n>m:
        for i in range(n):
            if i%2==0:
                s.add(i)
                if n-len(s)==m:
                    break
        for i in range(n):
            if i not in s:
                for j in range(m):
                    print(arr[i][j],end=' ')
                print()
    elif n<m:
        for i in range(n):
            for j in range(m):
                if j%2==1:
                    s.add(j)
                    if m-len(s)==n: break
        for i in range(n):
            for j in range(m):
                if j not in s:
                    print(arr[i][j],end=' ')
            print()
    else:
        for i in range(n):
            for j in range(m):
                print(arr[i][j],end=' ')
            print()
