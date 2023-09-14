from math import *

def nt(n):
   

    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    
    return True
def dao(n):
    sum,ans=0,n
    while n !=0:
        sum=sum*10+n%10
        n //=10
    
    return sum
if __name__=='__main__':
    for i in range(int(input())):
        n=int(input())
        visit=[False]*1000000
        for i in range(n):
            if visit[i]==False:
                if nt(i) and nt(dao(i)) and (i != dao(i)):
                    visit[i]=True
                    visit[dao(i)]=True
                    if i< n and dao(i)<n:
                        print(i,dao(i),end=' ')
        print()
        
        
            

            


        