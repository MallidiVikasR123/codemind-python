n=int(input())
s=n*n
sm=0
while s:
    sm+=s%10
    s//=10
if sm==n:
    print("Neon Number")
else:
    print("Not Neon Number")