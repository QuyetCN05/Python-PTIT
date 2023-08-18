def check(s):
    a=list(s)
    for i in range(0,len(a)-1):
        if int(a[i]) >int(a[i+1]):
            return False
        
    return True

if __name__=='__main__':
    t=int(input())
    while t !=0:
        t-=1
        s=input()
        if(check(s)):
            print('YES')
        else:
            print('NO')