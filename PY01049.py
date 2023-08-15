from math import *


def check(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        s = input()
        cnt = 0
        for j in s:
            if (check(int(j))):
                cnt += 1
        a = len(s)-cnt
        if (check(len(s)) and (cnt > a)):
            print('YES')
        else:
            print('NO')
