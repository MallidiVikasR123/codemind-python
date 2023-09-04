n=int(input())
a=list(map(int,input().split()))
c=n/2
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]>c:
        print(i)