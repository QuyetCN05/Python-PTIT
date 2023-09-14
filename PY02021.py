
if __name__=='__main__':
    for i in range(int(input())):
        n,m,p=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=list(map(int,input().split()))
        i,j,k=0,0,0
        d=[]
        while i<n and j<m and k<p:
            if a[i]==b[j] and b[j]==c[k]:
                d.append(a[i])
                i+=1;j+=1;k+=1
            elif a[i]<=b[j] and a[i]<=c[k]: i+=1
            elif b[j]<=a[i] and b[j]<=c[k]: j+=1
            else: k+=1
        if len(d)==0:
            print('NO')
        else:
            for x in d:
                print(x,end=' ')
            print()

        
