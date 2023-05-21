n=int(input())
sum=0
while n>=10:
    t=n
    sum=0
    while t:
        sum+=(t%10)**2
        t//=10
    n=sum
print((n==1 or n==7))