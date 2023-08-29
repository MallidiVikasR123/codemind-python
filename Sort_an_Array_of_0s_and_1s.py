n=int(input())
a=list(map(int,input().split()))
z=a.count(0)
o=a.count(1)
r=[]
for i in range(z):
    r.append(0)
for i in range(o):
    r.append(1)
print(*r)