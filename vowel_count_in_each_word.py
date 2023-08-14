s=input()
l=[]
a=0
for i in s:
    if i!=" " and i in "aeiouAEIOU":
        a+=1
    elif i==" ":
        l.append(a)
        a=0
l.append(a)
print(*l)