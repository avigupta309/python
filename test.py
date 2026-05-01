number=[12,1,5,9,4,2,1,5,5,12]
new=[]
dup={}

for n in number:
    if n not in new:
        new.append(n)
        dup[n]=1 
    else:
        dup[n]+=1
      

print(new)
print(dup)