n=int(input())
while(n>9):
    temp=n;
    s=0;
    while(temp):
        s+=temp%10;
        temp//=10;
    n=s
print(n)

    