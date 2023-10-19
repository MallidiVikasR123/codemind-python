for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    c.extend(a)
    c.extend(b)
    c=set(c)
    r=((((n+1)*n)/2)-sum(c))
    if r==0:print("YES")
    else:print("NO")