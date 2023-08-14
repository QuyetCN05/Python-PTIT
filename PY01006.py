import math
def check(s):
    cnt=0
    for i in s:
        if(i== '4' or i=='7'):
            cnt+=1
    return (cnt==len(s))
    
if __name__=='__main__':
    t=int(input())
    for i in range(1,t+1):
        s=input()
        if(check(s)):
            print('YES')
        else:
            print('NO')
    
       
   
    


