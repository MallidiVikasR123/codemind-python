n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in l:
    if i not in ll:
        ll.append(i)
print(*ll)