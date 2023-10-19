n=int(input())
a=1
b=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if  j==a or j==b:
            print("x",end="")
        else:
            print("0",end="")
    a+=1
    b-=1
    print()