def is_prime(n):
    if n==1: return 0
    for i in range(2,int(n**(0.5))+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
m=int(input())
s=0
for j in range(n,m+1):
    if is_prime(j): s+=1
print(s)