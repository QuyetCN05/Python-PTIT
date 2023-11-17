from math import *
import io, os, sys, time
import array as arr

def kiem_tra(a, pos):
    for i in range(len(a)):
        if a[i] // pos == a[i] // (pos + 1): return False
    return True

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    b = arr[::]
    for i in range(b[0], -1, -1):
        if kiem_tra(arr, i):
            for j in range(n): ans += arr[j] // (i + 1) + 1
            break
    print(ans)