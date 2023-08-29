s=input()
c=0
for i in s:
    n=ord(i)
    if n>=47 and n<58:
        c+=int(i)
print(c)