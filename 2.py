print("l: ",end="")
l=float(input())

print("n: ",end="")
n=float(input())

print("q: ",end="")
q=float(input())

K1=(l**2+n**2)
K2=l/n*q
if l<n:
    K2=(l-n)*q
print("K1: ",K1," K2: ",K2)

if K2>K1:
    print("K2=Kmax=",K2)
elif K2<K1:
    print("K1=Kmax=",K1)
else:
    print("K2=K1=",K1)
