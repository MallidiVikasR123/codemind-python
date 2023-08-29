s=input()
w=""
r=""
for i in range(len(s)-1,-1,-1):
    if s[i]!=" ":
        w+=s[i]
    elif s[i]==" ":
        r+=w[::-1]+" "
        w=""
else:
    r+=w[::-1]
print(r)