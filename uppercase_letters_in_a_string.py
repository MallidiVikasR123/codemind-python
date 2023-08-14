s=input();a=0
for i in s:
    c=ord(i)
    if c>64 and c<91:
        a+=1
print(a)