n=int(input())
a,b,c=0,1,0
if n==0 or n==1:
    print(True)
else:
    while c<n:
        c=a+b
        a=b
        b=c
    print(c==n)