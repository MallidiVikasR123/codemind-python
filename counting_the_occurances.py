s=input()
k=input()
c=0
for i in s:
    if k==i:c+=1
if c==0:print("-1")
else:print(c)