n=int(input())
a=list(map(int,input().split()))
b=int(input())
i=0
r=[]
while(b<n):
    r.append(a[i])
    r.append(a[b])
    i+=1
    b+=1
print(*r)