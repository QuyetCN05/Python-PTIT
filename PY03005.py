from collections import *
from functools import *
from math import *
import os, sys, time, io
import re

if __name__ == "__main__":
    se = set()
    for i in range(48, 58):
        se.add(chr(i))
    for j in range(65, 91):
        se.add(chr(j))
    for j in range(97, 123):
        se.add(chr(j))
    a = []
    n, t = map(int, input().split())
    for i in range(n):
        s = input().lower()
        res = ""
        for x in s:
            if x in se:
                res += x
            elif x not in se:
                res += " "
        for j in res.split():
            a.append(j)
    counter = list(Counter(a).items())
    counter.sort(key=lambda x: (-x[1], x[0]))
    for x in counter:
        if x[1] >= t:
            for j in x:
                print(j, end=" ")
            print()
