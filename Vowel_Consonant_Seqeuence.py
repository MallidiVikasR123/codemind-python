r=input()
s=''
for i in r:
    if i in "aeiouAEIOU":
        s+='V'
    else:s+='C'
            
ans=""
n=len(s);i=0;
while(i<n):
    if(s[i]=='C'):
        while(i<n and s[i]=='C'): i+=1;
        ans+='C';
        
    else:
        while(i<n and s[i]=='V'): i+=1;
        ans+='V';
print(ans)