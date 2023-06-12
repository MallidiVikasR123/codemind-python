n=input()
c=[]
for i in n:
    if i not in c:
        c.append(i)
if len(n)==len(c):
    print("Unique Number")
else:
    print("Not Unique Number")