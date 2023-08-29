for t in range(int(input())):
    s=input()
    for i in s:
        n=ord(i)
        if n>=47 and n<58:
            print("Yes")
            break
    else:
        print("No")
            