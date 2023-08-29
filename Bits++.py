n=int(input())
x=0
c=0
for i in range(n):
    s=input()
    if "++" in s:
        c+=1
    elif "--" in s:
        c-=1
print(c)