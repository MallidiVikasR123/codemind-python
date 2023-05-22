n,m=map(int,input().split())
x=str(n)
x1=m+1
a,b=x[:m],x[:-x1:-1][::-1]
print(abs(int(a)-int(b)))