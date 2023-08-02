n=int(input())
l=list(map(int,input().split()))
r=0
for i in range(n):
    if l[i]%2!=0:break
    else:r+=l[i]
print(r)