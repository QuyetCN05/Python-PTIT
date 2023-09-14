from math import *


def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True

if __name__=='__main__':
    for i in range(int(input())):
        n=int(input())
        cnt=0
        for i in range(n):
            if nt(i) and nt(i+4) and nt(i+6):
                if i+4<n and i+6<n:
                    cnt+=1
            if nt(i) and nt(i+2) and nt(i+6):
                if i+2 <n and i+6 <n:
                    cnt+=1
        
        print(cnt)