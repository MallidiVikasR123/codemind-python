def palindrome(n):
    s=str(n)
    if(s==s[::-1]):
        return 1
    return 0
m=int(input())
n=int(input())
for i in range(m,n):
    if(palindrome(i)):
        print(i,end=' ')