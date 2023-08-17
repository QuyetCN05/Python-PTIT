from math import *


def check(n):
    a = n
    sum = 0
    while n != 0:
        sum = sum*10+n % 10
        n //= 10
    return (a == sum)

def nt(n):
    if n< 2: return False
    for i in range(2,isqrt(n)+1):
        if(n%i==0):
            return False
    
    return True


if __name__ == '__main__':
    t = int(input())
    while t != 0:
        t-=1
        s = input()
        sum = 0
        for i in s:
            sum += int(i)
        if(nt(sum)):
            print('YES')
        else:
            print('NO')
    
    
         
        

