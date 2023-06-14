n=int(input())
s=str(n)
e,o=0,0
for i in s:
    if(int(i)%2==0):e+=1
    elif(int(i)%2==1):o+=1
if(e==len(s)):print("Even")
elif(o==len(s)):print("Odd")
else:print("Mixed")