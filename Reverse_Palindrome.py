
def ispalindrome(n : int) -> bool :
    rev = 0
    temp = n
    while n != 0 :
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10
    if temp == rev :
        return True
    else :
        return False

def reverse(n : int) -> int :
    rev = 0
    while n != 0 :
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10
    return rev
    
    

n = int(input())
while True :
    a = reverse(n)
    n = a + n
    if ispalindrome(n) :
        print(n)
        break