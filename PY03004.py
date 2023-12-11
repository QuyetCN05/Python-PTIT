from collections import *
from functools import *
from math import *
import os, sys, time, io
import re

if __name__ == "__main__":
    d = set()
    # d.add(' ')
    for i in range(48, 58): d.add(chr(i))
    for i in range(65, 91): d.add(chr(i))
    for i in range(97, 123): d.add(chr(i))
    a = []
    for t in range(int(input())):
        s = input().lower()
        res = ''
        for x in s:
            if x in d: res += x
            elif x not in d: res += ' '
        for x in res.split(): a.append(x)
    counter = list(Counter(a).items())
    counter.sort(key = lambda x : (-x[1], x[0]))
    for x in counter:
        for y in x: print(y, end = ' ')
        print()
