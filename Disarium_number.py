n=input()
sz=len(n)
n=int(n)
sm,t=0,n
while n:
    sm+=(n%10)**sz
    sz-=1
    n//=10
print(t==sm)