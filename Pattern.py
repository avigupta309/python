## make triangle 
#1.
triangle=10
for i in range(1,triangle+1):
    print(" "*(triangle-i)+"*"*(2*i-1))


## making Arrow
print("\n\n\n\n\n\n\n")
row=10
for i in range(1,row+1):
    print(" "*(row-i)+"*"*(i*2-1))
for i in range(row+1):
    print(" "*(row//2)+"*"*row)


print("\n\n\n\n\n\n\n")

##making Temple
bulletRow=10
for i in range(1,bulletRow+1):
    print(" "*(bulletRow-i)+"B"*(i*2-1))
for j in range(bulletRow):
    print("B"*(bulletRow*2))
