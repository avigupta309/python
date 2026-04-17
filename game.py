import random
operations={
         '+': lambda a,b :a+b,
         '-':lambda a,b:a-b,
         '*':lambda a,b:a*b,
         '//':lambda a,b:a//b,
         '%':lambda a,b:a%b
      }

def calculateResult(op,num1,num2):
  return operations[op](num1,num2)


def generateQuestion():
   name=input("Enter Your Name :").upper().strip() 
   numberRange=int(input("Enter the Number Range : "))
   operator=['+',"-","*","//","%"]
   points,level=0,0
   while True:
      op=random.choice(operator)
      num1=random.randint(1,numberRange)
      num2=random.randint(1,numberRange)
      try:
         userAns=int(input(f"{num1} {op} {num2} = "))
      except:
         print("Enter Valid Value ")
         continue
      result=calculateResult(op,num1,num2)
      if userAns==result:
         points+=1
         level+=1
      else:
        print(f"Mr/Ms. {name}")
        print(f"You Miss The Game !!\nwith Points : {points}")
        print(f"The Correct Answer Is : {result}")
        break
      if level%5==0:
         print(f"Mr/Ms. {name}")
         print(f"Wow Youe Pass the Level {level//5}")
         print(f"The Total Points you Get : {points}")
         user=input("Want to Continue The Game : (yes/no) ? ").lower()
         if user=="no":
            break 

      
generateQuestion()