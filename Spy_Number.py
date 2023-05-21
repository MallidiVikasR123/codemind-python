n=int(input())
s,p=0,1
while n:
    s+=n%10
    p*=n%10
    n//=10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")