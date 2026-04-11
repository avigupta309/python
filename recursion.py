arra=[10,20,30,40,50]

n=len(arra)

for i in range(n):
    swapped=False
    for j in range(0,n-i-1):
        if arra[j]>arra[j+1]:
            arra[j],arra[j+1]=arra[j+1],arra[j]
            swapped=True
    if not swapped:
        break

print(arra)