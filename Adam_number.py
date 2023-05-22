n=int(input())
x=int(str(n)[::-1])
x1=x*x
x1=int(str(x1)[::-1])
if((n*n)==x1):print("True")
else:print("False")