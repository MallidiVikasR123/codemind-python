n=int(input())
a=list(map(int,input().split()))
s=sum(a)
while(n):
    if s%n==0:break
    else:n-=1
print(n)