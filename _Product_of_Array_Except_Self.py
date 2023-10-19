n=int(input())
a=list(map(int,input().split()))
p=1
r=[]
for i in a:
    p*=i
for j in a:
    r.append(int(p/j))
print(*r)