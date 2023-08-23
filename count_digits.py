n=int(input())
for i in list(map(int,input().split())):
    if i>=0:
        print(len(str(i)),end=" ")
    elif i<0:
        i=i*-1
        print(len(str(i)),end=" ")