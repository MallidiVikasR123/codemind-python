x=input()
l=[]
c=0
for i in x:
    if i!=" ":
        c+=1
    elif i==" ":
        l.append(c)
        c=0
l.append(c)
print(min(l))