def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def post_prime(n):
    upper = n + 1
    while True:
        if is_prime(upper):
            return upper
        upper += 1

n1=int(input())
n2=int(input())
ans=post_prime(n1+n2)
print(ans-(n1+n2))