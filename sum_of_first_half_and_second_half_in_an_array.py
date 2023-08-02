n=int(input())
l=list(map(int,input().split()))
r,s=0,0
for i in range(n):
    if i<(n//2):
        r+=l[i]
    else:
        s+=l[i]
print(r,s,sep="
")