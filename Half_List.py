n=int(input())
a=list(map(int,input().split()))
h=n//2
r=[]
for i in range(n-1,h-1,-1):
    r.append(a[i])
r.extend(a[:h])
print(*r)