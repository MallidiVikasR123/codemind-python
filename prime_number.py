n=int(input())
cnt=0
for i in range(2,n):
    if n%i==0:
        cnt+=1
print("prime") if not cnt else print("not a prime")