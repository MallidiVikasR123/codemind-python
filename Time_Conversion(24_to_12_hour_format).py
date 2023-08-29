s=input()
i=s[:2]
if int(i)<=12:
    if i=="00":
        print("12"+s[2:]+" AM")
    elif i=="12":
        print(s+" PM")
    else:
        print(s+" AM")
elif int(i)>12:
    r=str(int(i)-12)
    if int(r)<10:
        print(s.replace(i,"0"+r,1)+" PM")
    else:
        print(s.replace(i,r,1)+" PM")