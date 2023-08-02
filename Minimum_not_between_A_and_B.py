n=int(input())
l=list(map(int,input().split()))
x,y=map(int,input().split())
i=0;m=max(l)
while(i<n):
    if l[i]<x or l[i]>y:
        m=min(m,l[i])
    i+=1
if m==max(l):
    print(-1)
else:
    print(m)
        