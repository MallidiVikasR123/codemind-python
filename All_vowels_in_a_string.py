x=input()
s="aeoiu"
for i in s:
    if i not in x:
        print("False")
        break
else:print("True")