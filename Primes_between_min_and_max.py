import math
def prime(n):
    if n<=1:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):return 0
    return n
n=int(input())
l=list(map(int,input().split()))
a=l.index(max(l));r=0;
b=l.index(min(l));l1=[]
if  b<=a:
    for i in range(b,a+1):
        if prime(l[i]) and l[i] not in l1:
            l1.append(l[i])
            r+=1
elif  a<b:
    for i in range(a,b+1):
        if prime(l[i]) and l[i] not in l1:
            l1.append(l[i])
            r+=1
print(r)