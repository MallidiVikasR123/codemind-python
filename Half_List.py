n=int(input())
a=list(map(int,input().split()))
h=n//2
r=[]
r.extend(a[h:][::-1])
r.extend(a[:h])
print(*r)