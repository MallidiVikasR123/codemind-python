def palin(s):
    s1=s[::-1]
    if s==s1:return True
    return False
print(palin(input().lower()))