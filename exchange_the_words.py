x=input()
s="";r=""
for i in x:
    if i!=" ":
        s+=i
    elif i==" ":
        r=" "+s+r
        s=""
r=s+r
print(r)
