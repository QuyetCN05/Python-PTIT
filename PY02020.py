

if __name__=='__main__':
    n=int(input())
    a=list(map(float,input().split()))
    y=max(a)
    x=min(a)
    for i in a:
        if i==y:
            a.remove(i)
        if i==x:
            a.remove(i)
    print('{:.2f}'.format(sum(a)/len(a)))