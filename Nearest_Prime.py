def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
def pre(n):
    while is_prime(n)==0:
        n-=1
    return n
def nextp(n):
    while is_prime(n)==0:
        n+=1
    return n
t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=n-pre(n)
    b=nextp(n)-n
    if a<b:
        print(pre(n))
    elif a==b:
        print(pre(n))
    else:
        print(nextp(n))