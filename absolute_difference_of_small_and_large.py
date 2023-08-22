s=input()
w=""
mn=0
mx=0
for i in s:
    if i!=" ":
        w+=i
    if i==" ":
        mn=ord(min(w))
        mx=ord(max(w))
        print(abs(mn-mx),end=" ")
        w=""
else:
    mn=ord(min(w))
    mx=ord(max(w))
    print(abs(mn-mx))