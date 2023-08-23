n=int(input())
a=list(map(int,input().split()))
for i in a:
    if i>=0:
        print(len(str(i)),end=" ")
    else:
        i=i*-1
        print(len(str(i)),end=" ")
    