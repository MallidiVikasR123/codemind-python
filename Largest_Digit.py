n=input()
m=n[0]
for i in range(len(n)):
    if(m<n[i]):
        m=n[i]
print(m)