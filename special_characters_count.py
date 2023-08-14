a=input()
c=0
for i in a:
    if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and i!=" ":
        c+=1
    
print(c)