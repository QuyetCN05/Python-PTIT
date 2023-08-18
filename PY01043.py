
from math import *

def nt(n):
    a=n
    tmp=0
    while n !=0:
        tmp=tmp*10+n%10
        n //=10
    
    return(tmp==a)
def check(n):
    while n !=0:
        a=n%10
        if(a != 0 and a != 2 and a!=4 and a !=6 and a !=8):
            return False
        n //=10
    return True

def tinh(n):
    cnt=0
    while n !=0:
        n //=10
        cnt+=1

    return (cnt%2==0)

if __name__=='__main__':
    t=int(input())
    while t !=0:
        t-=1
        n=int(input())
        for i in range(22,n):
            if(check(i) and nt(i) and tinh(i)):
                print(i,end=' ')
        print()
       