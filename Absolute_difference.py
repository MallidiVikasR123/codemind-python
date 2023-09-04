def prime(n):
    if n<2:return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
p,np=1,1
for _ in a:
    if prime(_):p*=_
    else:np*=_
print(abs(p-np))