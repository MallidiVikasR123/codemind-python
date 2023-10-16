for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if a==b:print("0")
    else:print(abs(b[0]-b[-1]))