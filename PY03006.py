from collections import *
from functools import *
from math import *
import os, sys, time, io
import re

if __name__ == "__main__":
    se = set()
    for i in range(65, 91):
        se.add(chr(i))
    for i in range(97, 123):
        se.add(chr(i))
    a = []
    for t in range(int(input())):
        s = input().lower()
        res = ""
        for x in s:
            if x in se:
                res += x
            elif x not in se:
                res += " "
        for x in res.split():
            a.append(x)
    counter = list(Counter(a).items())
    counter.sort(key=lambda x: (-x[1], x[0]))
    for x in counter:
        for y in x:
            print(y, end=" ")
        print()
