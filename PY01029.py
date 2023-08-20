from math import *


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        a = s[::-1]
        if (gcd(int(s), int(a)) == 1):
            print('YES')
        else:
            print('NO')
