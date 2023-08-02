import math
def prime(n):
    if n==1:
        return -1
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):return -1
    return n
n=int(input())
l=list(map(int,input().split()))
#k=int(input())
a=0
for i in l:
    if prime(i)==i:
        a+=1
print("%d"%(a))