from math import *
from sys import stdin


if __name__ == '__main__':
    n,m=map(int,input().split())
    a=[]
    visited=[[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        b=list(map(int,stdin.readline().split()))
        a.append(b)
    c=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    cnt=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==-1:
                for x in c:
                    e,f=i+x[0],j+x[1]
                    if e>=0 and e<n and f>=0 and f<m and not visited[e][f]:
                        visited[e][f]=True
                        cnt+=a[e][f]
    print(cnt)

   

    
    