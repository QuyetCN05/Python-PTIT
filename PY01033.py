
from math import *
if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b+1):
        for j in range(i+1, b+1):
            if gcd(i, j) == 1:
                for t in range(j+1, b+1):
                    if gcd(j, t) == 1:
                        if gcd(i, t) == 1:
                            print('(', i, ', ', j, ', ', t, ')', sep='')
