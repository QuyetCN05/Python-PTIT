from math import *


if __name__ == '__main__':
    n, k = map(int, input().split())
    res = 10**k
    ans = 10**(k-1)
    cnt = 0
    for i in range(ans, res):
        if gcd(n, i) == 1:
            cnt += 1
            print(i, end=' ')
            if cnt == 10:
                cnt = 0
                print()
