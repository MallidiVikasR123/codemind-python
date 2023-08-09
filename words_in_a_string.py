x=input()
l=[]
c=1
for i in x:
    if i==" ":
        c+=1
        l.append(c)
    elif i!=" ":
        
        c=0
l.append(c)
print(len(l))