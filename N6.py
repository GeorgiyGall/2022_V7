a=[]
min=0
indxmin=0

for i in range(10):
    print("a[",i,"]=",end="")
    a.append(float(input()))
    if i==0:
        min=a[i]
    else:
        if min>a[i]:
            min=a[i]
            indxmin=i
    print("i==", i , "a[i]: ",a[i],  " min: ", min)

print(a)

print("indxmin=", indxmin, "min=", min)

if indxmin+1<5:
    for i in range(10):
        if a[i]<0:
            a[i]=min

print(a)
