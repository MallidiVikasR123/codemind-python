n=int(input())
l=list(map(int,input().split()))
o,e=0,0
for i in range(n-1,-1,-1):
    if(l[i]%2==0):
        e+=l[i]
for i in range(n-1,-1,-1):
    if(l[i]%2==1):
        o+=l[i]
print(abs(o-e))