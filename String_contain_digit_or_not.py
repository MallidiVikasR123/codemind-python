s=input()
c=0
for i in s:
    n=ord(i)
    if n>=47 and n<58:
        c+=1
if c==0:print("Doesn't contain digit")
else:print(f"Contains {c} digit")