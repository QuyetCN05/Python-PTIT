def check(s):
    for i in range(len(s)):
        if s[i] !='0' and s[i] !='1' and s[i] !='2':
            return False
    
    return True
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        b=set()
        arr=list(s)
        for i in arr:
            b.add(i)
        if (len(b)==1 or len(b)==2 or len(b)==3) and check(s):
            print('YES')
        else:
            print('NO')
