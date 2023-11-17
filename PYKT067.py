from itertools import *
from math import *
from collections import *
from functools import *

if __name__=='__main__':
    for i in range(int(input())):
        n=int(input())
        perm=permutations([x for x in range(1,n+1)])
        a=list(perm)
        a.sort(reverse=True)
        print(len(a))
        for per in a:
            for x in per:
                print(x,end='')
            print(end=' ')
        print()
        