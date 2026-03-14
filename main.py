str="ipsumdolorsitametconsecteturadipiscingelittemporincididuntutlab"
strArr=[
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
  "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
  "u", "v", "w", "x", "y", "z"
]


newArray=[0]*26

for ch in str:
    asci=ord(ch)
    index=asci-97
    newArray[index]+=1

for sr in strArr:
    asci=ord(sr)
    index=asci-97
    print(newArray[index])

# newArr=[0]*26
# for ch in str:
#     asci=ord(ch)
#     index=asci-97
#     newArr[index]+=1


# for item in strArr:
#     asci=ord(item) 
#     index=asci-97
#     print(f'{item}={newArr[index]}')
