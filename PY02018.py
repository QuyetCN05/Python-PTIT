from collections import *

if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    check=False
    for i in range(1,n):
        if a[i] != a[i-1] and a[i] !=a[i-1]+1:
            print(a[i-1]+1)
            check=True
            break
    if check==False:
        print(max(a)+1)