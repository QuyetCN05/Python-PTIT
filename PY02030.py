from collections import *
from functools import *
from math import *


def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

# def check_1(arr):

#     for i in range(len(arr)):
#         sum=0
#         for j in range(i+1):
#             sum+=arr[j]
#         if nt(sum):
#             return i
#     return -1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b, d = [], {}
    for x in a:
        if x not in d:
            b.append(x)
            d[x] = 1
    res = -1
    for i in range(len(b)):
        if nt(sum(b[:i+1])) and nt(sum(b[i+1:])):
            res = i
            break
    if res == -1:
        print('NOT FOUND')
    else:
        print(res)
