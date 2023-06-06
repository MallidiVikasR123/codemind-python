n=int(input())
l=list(map(int,input().split()))
e=0
for i in range(0,n,2):
    e+=l[i]
print(e)