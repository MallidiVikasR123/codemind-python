s=input();w="";c=0
for i in s:
    if i!=" ":
        w+=i
        #print(w)
    elif i==" ":
        if w[0] in 'aeiouAEIOU' and w[-1] not in "aeiouAEIOU":
           c+=1
        w=""
else:
    if w[0] in 'aeiouAEIOU' and w[-1] not in "aeiouAEIOU":
        c+=1
print(c)