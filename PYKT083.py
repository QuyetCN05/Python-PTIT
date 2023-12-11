from collections import *
from functools import *
from math import *
import io, os, sys, time
from datetime import datetime


if __name__ == "__main__":
    n = int(input())
    d = dict()
    se = set()
    for i in range(n):
        s = input().split()
        if s[-2] == "IN":
            if s[-1] not in se:
                se.add(s[-1])
                if s[1] == "Xe_con" and s[2] == "5":
                    d[s[-1]] = 10000
                elif s[1] == "Xe_con" and s[2] == "7":
                    d[s[-1]] = 15000
                elif s[1] == "Xe_tai" and s[2] == "2":
                    d[s[-1]] = 20000
                elif s[1] == "Xe_khach" and s[2] == "29":
                    d[s[-1]] = 50000
                else:
                    d[s[-1]] = 70000
            else:
                if s[1] == "Xe_con" and s[2] == "5":
                    d[s[-1]] = d.get(s[-1]) + 10000
                elif s[1] == "Xe_con" and s[2] == "7":
                    d[s[-1]] = d.get(s[-1]) + 15000
                elif s[1] == "Xe_tai" and s[2] == "2":
                    d[s[-1]] = d.get(s[-1]) + 20000
                elif s[1] == "Xe_khach" and s[2] == "29":
                    d[s[-1]] = d.get(s[-1]) + 50000
                else:
                    d[s[-1]] = d.get(s[-1]) + 70000
    for j in d.keys():
        print(j, d[j], sep=": ")
