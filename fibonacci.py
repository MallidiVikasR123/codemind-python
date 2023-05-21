n=int(input())
a,b,c=0,1,0
for i in range(n):
    print(a,end=' ')
    c=a+b
    a=b
    b=c