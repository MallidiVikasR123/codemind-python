x=input()
s="";r=""
for i in x:
    if i!=" ":
        s+=i
    elif i==" ":
        r+=s[::-1]+" "
        s=""
r+=s[::-1]
print(r)