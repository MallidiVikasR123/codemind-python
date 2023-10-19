for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(int((((n+1)*n)/2)-sum(a)))