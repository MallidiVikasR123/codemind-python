for i in range(int(input())):
    w=input()
    c=0
    for j in w:
        n=ord(j)
        if n>=47 and n<58:
            c+=1
    if c==len(w):print("True")
    else:print("False")