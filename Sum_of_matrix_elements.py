m=int(input())
n=int(input())
a=[]
c=0
for i in range(m):
    b=list(map(int,input().split()))
    a.append(b)
for j in a:
    c+=sum(j)
print(c)