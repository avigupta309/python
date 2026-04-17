## finding prime number 
#1.

def primeNumber(num):
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=False
            break
    
    if prime:
     print(f"{num} is  Prime")
    else:
       print(f"{num} is not Prime")

num=int(input("Enter the Number : "))
primeNumber(num)




#2.

def primeNumbers(num):
   prime=[]
   for i in range(2,num):
      isPrime=True
      for j in range(2,int(i**0.5)+1):
         if i%j==0:
            isPrime=False
            break
      if isPrime:
           prime.append(i)
   return prime
      
num=int(input("Enter Any Number : "))
returnResult=primeNumbers(num)
print(returnResult)



#3.

def primeRangeNumber(start,end):
    prime=[]
    for i in range(start,end):
        isPrime=True
        for j in range(2,int(i**0.5)+1):
            if i %j==0:
                isPrime=False
                break
        if isPrime:
            prime.append(i)
    print(prime)

start=int(input("Enter Starting Number : "))
end=int(input("Enter Ending Number : "))
primeRangeNumber(start,end)



print("prime message")