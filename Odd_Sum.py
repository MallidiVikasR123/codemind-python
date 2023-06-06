n=int(input())
l=list(map(int,input().split()))
e=0
for i in range(n):
    if(l[i]%2==1):
        e+=l[i]
print(e)