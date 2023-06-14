import math
x,y,m=map(int,input().split())
s=math.pow(x,y)
print(int(s%m))