def palindrome(n):
    x=int(str(n)[::-1])
    if(n==x):return 1
    else:return 0
def add(n):
    a=int(str(n)[::-1])
    b=n+a
    if(palindrome(b)==1):
        print(b)
    else:add(b)
n=int(input())
add(n)