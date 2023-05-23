import math
n=int(input())
l=list(map(int,input().split()))
j=math.gcd(*l)
print(j)