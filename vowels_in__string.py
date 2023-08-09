c=0;l=[]
for i in input():
    if i in 'aeiouAEIOU' and i not in l:
        l.append(i)
        print(i,end=" ")
        c=1
else:
    if c==0:
        print("-1")