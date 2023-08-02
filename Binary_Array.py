n=int(input())
arr=list(map(int,input().split()))
s=1
for i in arr:
    if i>1:
        s=0
        break
if s==1:print("True")
elif s==0:print("False")