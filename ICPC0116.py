
if __name__=='__main__':
    for i in range(int(input())):
        s=input()
        a=list(s)
        if(a[0]==a[len(a)-1]):
            print('YES')
        else:
            print('NO')