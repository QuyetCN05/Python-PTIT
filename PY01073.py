from itertools import *

if __name__=='__main__':
    s=input()
    perm=permutations(s)
    for i in perm:
        for j in i:
            print(j,end='')
        print()