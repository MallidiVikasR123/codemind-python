h,m=map(int,input().split(":"))
h=h+m/60
z=abs(h*30-m*6)
print(z) if z<=180 else print(360-z)