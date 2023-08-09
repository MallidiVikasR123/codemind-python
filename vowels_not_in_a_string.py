x=input()
a='aeiou';c=0
for i in a:
    if i not in x:
        print(i,end=" ")
        c=1
else:
    if c==0:print("0")