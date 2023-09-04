n=int(input())
a=list(map(int,input().split(" ")))
e=0;o=0
for i in range(0,n,2):
    e+=a[i];
    if i<n-1:o+=a[i+1]
if e-o==0:print("YES")
else:print("NO")