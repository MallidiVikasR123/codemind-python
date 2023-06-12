def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def pre_prime(n):
    lower = n 
    while lower >= 2:
        if is_prime(lower):
            return lower
        lower -= 1
def post_prime(n):
    upper = n 
    while True:
        if is_prime(upper):
            return upper
        upper += 1

t=int(input())
for i in range(t):
    n=int(input())
    c=pre_prime(n)
    s=post_prime(n)
    if((s-n)==(n-c)):
        print(c)
    elif((s-n)<(n-c)):
        print(s)
    else:
        print(c)