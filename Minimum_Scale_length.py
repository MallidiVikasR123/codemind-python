n=int(input())
l=list(map(int,input().split()))
for i in range(max(l)+1,1,-1):
    c=0
    for j in l:
        if(j%i==0):
            c+=1
    if(c==len(l)):
        print(i)
        break
else:print("1")