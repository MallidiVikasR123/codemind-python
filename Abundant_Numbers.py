n=int(input())
sm=0
for i in range(1,n):
    if n%i==0:
        sm+=i
print(sm>n)