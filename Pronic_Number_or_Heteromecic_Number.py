n,i=int(input()),1
while(i*(i+1)<=n): i+=1
if i*(i-1)==n:
    print("YES")
else:
    print("NO")