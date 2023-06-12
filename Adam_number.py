n=input()
m=n[::-1]
sn=int(n)*int(n)
sm=int(m)*int(m)
if str(sn)==str(sm)[::-1]:
    print("True")
else:
    print("False")