f=open('DATA1.in','r')
p=open('DATA2.in','r')
b=set()
c=set()
for line in f:
    if line[-1]=='/n':
        a=line[:-1].lower().split()
        for x in a:
            b.add(x)
    else:
        a=line.lower().split()
        for x in a:
            b.add(x)
for line in p:
    if line[-1]=='/n':
        a=line[:-1].lower().split()
        for x in a:
            c.add(x)
    else:
        a=line.lower().split()
        for x in a:
            c.add(x)
u=b-c
v=c-b
arr=list(u)
brr=list(v)
arr.sort()
brr.sort()
# arr=list(u).sort()
# brr=list(v).sort()
# for x in arr:
#     print(x,end=' ')
# print()
# for x in brr:
#     print(x,end=' ')
for i in arr:
    print(i,end=' ')
print()
for j in brr:
    print(j,end=' ')