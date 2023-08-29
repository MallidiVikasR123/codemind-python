s=input()
a=s[:5]
b=s[2:5]
if s[-2:]=="AM":
    if s[:2]=="12": print("00"+b)
    else:print(a)
else:
    if s[:2]=="12": print(a)
    else:
        r=int(s[:2])+12
        print(str(r)+b)