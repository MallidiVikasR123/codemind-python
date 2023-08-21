def palin(s):
    s1=s[::-1]
    if s==s1:
        return 1
    return 0
st=input().lower()
s=""
c=0
for i in st:
    if i!=" ":
        s+=i
    elif i==" ":
        if palin(s):
            c+=1
        s=""
if palin(s):
    c+=1
print(c)