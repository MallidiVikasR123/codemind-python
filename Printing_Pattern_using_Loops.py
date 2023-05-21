n=int(input())
t=0
l=0
r=(n<<1)-1
b=r
for i in range(0,r):
    for j in range(0,r):
        print(n-(min(i-t,b-i-1,j-l,r-j-1)),end=' ')
    print()