n=int(input())
a=list(map(int,input().split()))
r=[]
for i in a:
    if i!=0:
        r.append(i)
for j in range(a.count(0)):
    r.append(0)
print(*r)  