s=input()
x,y=0,0
for i in s:
    if i=="z":x+=1
    else:y+=1
if y==2*x: print("Yes")
else:print("No")