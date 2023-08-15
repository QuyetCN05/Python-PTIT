from math import *
def check(n):
    if n< 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True




if __name__=='__main__':
    t=int(input())
    for i in range(1,t+1):
        s=input()
        str=''
        a=list(s)
        for j in range(-4,0,1):
            str+=a[j]
        if(check(int(str))):
            print('YES')
        else:
            print('NO')
    