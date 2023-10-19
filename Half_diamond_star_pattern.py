n=int(input())
if n>=3 and n<=100:
    i=1
    c=1
    while(i):
        for j in range(1,i+1):
            print("*",end="")
        print()
        c+=1
        if c<=n:
            i+=1
        elif c>n:i-=1
else:
    print("The pattern is not possible")
        