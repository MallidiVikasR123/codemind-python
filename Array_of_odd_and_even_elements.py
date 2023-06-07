n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if(i%2==0):
        e.append(i)
    elif(i%2==1):
        o.append(i)
o.extend(e)
for i in o:
    print(i,end=" ")
