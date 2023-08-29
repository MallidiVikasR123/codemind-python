s=input()
c=0
for i in s:
    n=ord(i)
    if n>=48 and n<58: c+=int(i)
print(c)