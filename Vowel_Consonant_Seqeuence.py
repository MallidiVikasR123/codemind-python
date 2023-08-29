s=input()
a=""
r=""
for i in s:
    if i not in "aeiouAEIOU":r+="C"
    elif i in "aeiouAEIOU":r+="V"
i=0
l=len(r)
while(i<l):
    if r[i]=="C":
        a+="C"
        while(i<l and r[i]!="V"): i+=1
    else:
        a+="V"
        while(i<l and r[i]!="C"): i+=1
print(a)