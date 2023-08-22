s=input()
a=""
b=""
for i in s:
    if i!=" ":
        a+=i
    elif i==" ":
        break;
for i in s[::-1]:
    if i!=" ":
        b+=i
    elif i==" ":
        break;
print(min(a),max(b))
    
            