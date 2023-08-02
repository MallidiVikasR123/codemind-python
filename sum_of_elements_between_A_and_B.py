n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
li=[]
for i in l:
    if i>=a and i<=b:
        li.append(i)

print(sum(li))