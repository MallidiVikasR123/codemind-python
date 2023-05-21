n=int(input())
c=0
if n<0:
    c=1
    n=-n
rev=0
while(n):
    rev=rev*10+(n%10)
    n//=10
print(-rev) if c else print(rev)