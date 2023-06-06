n=int(input())
a=list(map(int,input().split()))
a1=sum(a)/n
if int(a1) in a:
    print("True")
else:
    print("False")