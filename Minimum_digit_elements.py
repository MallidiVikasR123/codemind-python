n=int(input())
l=list(map(int,input().split()))
r=len(str(min(l)));c=0
for i in l:
    if r==len(str(i)):
        c+=1
print(c)