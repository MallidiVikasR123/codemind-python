n=int(input())
while(n>9):
    s=n
    su=0
    while(s):
        r=s%10
        su=su+r
        s=s//10
    n=su
print(n)      
        