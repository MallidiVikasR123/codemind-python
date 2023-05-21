n=int(input())
while n!=1:
    if n%2==0: n//=2
    if n%3==0: n//=3
    if n%5==0: n//=5
    if n!=1 and n%2!=0 and n%3!=0 and n%5!=0:
        print("Not Ugly Number")
        break
else: print("Ugly Number")