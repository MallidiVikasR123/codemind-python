s=input()
a=[]
c=0
for i in s:
    if i in "aeiou": c+=1
    else:
        a.append(c)
        c=0
else:
    a.append(c)
    c=0
print(max(a))