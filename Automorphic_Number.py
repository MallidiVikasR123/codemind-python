n=input()
sq=int(n)**2
l=len(n)
if sq%(10**l)==int(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")