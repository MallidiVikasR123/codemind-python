for _ in range(int(input())):
    s=input()
    a=[]
    n=0
    for i in s:
        a.append(int(i))
        n+=1
    su=0
    for j in range(min(a),max(a)+1):
        su+=j
    b=su-sum(a)
    if b==0:print("YES")
    else:print("NO")