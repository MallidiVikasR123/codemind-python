def palindrome(n):
    a=str(n)
    b=a[::-1]
    if(a==b):
        return 1
    return 0
n=int(input())
n1=n-1
n2=n+1
c,s=0,0
while(n1):
    if(palindrome(n1)):
        c=n1
        break
    else:
        n1=n1-1
while(n2):
    if(palindrome(n2)):
        s=n2
        break
    else:
        n2=n2+1
if((n-c)==(s-n)):
    print(c,s)
elif((n-c)<(s-n)):
    print(c)
else:
    print(s)