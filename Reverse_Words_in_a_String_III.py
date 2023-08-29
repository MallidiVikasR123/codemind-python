s=input()
w=""
r=""
for i in s:
    if i!=" ":
        w+=i
    elif i==" ":
        r+=w[::-1]+" "
        w=""
else:
    r+=w[::-1]
print(r)