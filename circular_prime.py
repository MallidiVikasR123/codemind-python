def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
n1=int(str(n)[::-1])
if(is_prime(n)==1 and is_prime(n1)==1):
    print("circular prime")
elif(is_prime(n)==1 and is_prime(n1)!=1):
    print("prime but not a circular prime")
elif(is_prime(n)==0 and is_prime(n1)==1):
    print("prime but not a circular prime")
elif(is_prime(n)!=1 and is_prime(n1)!=1):
    print("not prime")