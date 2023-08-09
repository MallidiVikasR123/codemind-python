x=input()
s="";r="";c=0
for i in x:
    if i!=" ":
        s+=i
    elif i==" " and c==0:
        r+=s[::-1]+" "
        s=""
        c=1
    elif i==" " and c==1:
        r+=s+" "
        s=""
        c=0
else:
    if c==1:
        r+=s
    elif c==0:
        r+=s[::-1]
print(r)