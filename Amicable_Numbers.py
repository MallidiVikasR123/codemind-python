a=int(input())
b=int(input())
asum,bsum=0,0
for i in range(1,a):
    if a%i==0:
        asum+=i
for i in range(1,b):
    if b%i==0:
        bsum+=i
if asum==b and bsum==a:
    print("Amicable")
else:
    print("Not Amicable")