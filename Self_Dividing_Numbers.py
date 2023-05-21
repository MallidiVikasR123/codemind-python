a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    c,s=0,0
    r=1
    while(n%10!=0 and n!=0):
        r=n%10
        if(r!=0):s+=1
        if(i%r==0):c+=1
        n=n//10
    if(c==s and c!=0 and s!=0):print(i,end=" ")
        