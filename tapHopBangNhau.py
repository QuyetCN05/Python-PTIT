n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = set(a)
d = set(b)
if c == d:
    print("YES")
else:
    print("NO")