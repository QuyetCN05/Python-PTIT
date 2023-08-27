from math import *

def nt(n):
    if n<2:
        return False
    
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True


def check_1(s):
    cnt=0
    for i in s:
        if nt(int(i)):
            cnt+=1
    
    return(cnt >len(s)-cnt)

if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        if nt(len(s)) and check_1(s):
            print('YES')
        else:
            print('NO')
