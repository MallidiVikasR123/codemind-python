def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**(0.5))+1):
        if(n%i==0):return 0
    return 1
n=int(input())
m=int(input())
s=n+m+1
while((n+m)):
    if(is_prime(s)):print(s-(n+m));break;
    else:s+=1