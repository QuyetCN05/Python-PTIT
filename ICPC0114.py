from math import*

def nt(n):
    a=int(n)
    if a<2:
        return False
    
    for i in range(2,isqrt(a)+1):
        if a%i==0:
            return False
    return True


def tong(n):
    a=int(n)
    sum=0
    while a !=0:
        sum +=a%10
        a //=10
    
    return sum

def check(n):
    a=int(n)

    while a !=0:
        cnt=a%10
        if(cnt !=2 and cnt !=3 and cnt !=5 and cnt !=7):
            return False
        
        a //=10
    
    return True

if __name__=='__main__':
    for i in range(int(input())):
        n=input()
        b=n[::-1]
        if(nt(int(n)) and nt(int(b)) and nt(tong(n)) and check(int(n))):
            print('YES')
        else:
            print('NO')

        