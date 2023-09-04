a=int(input())
b=list(map(int,input().split()))
r=0
for i in b:
    r=r*10+i
res=r+1
res=list(str(res))
print(*res)