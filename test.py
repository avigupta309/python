import random
def GameStart(num):
 points=0
 while True:
      operator=['+',"-","*","//","%"]
      number1=random.randint(1,num)
      number2=random.randint(1,num)
      op=random.choice(operator)
      userAns=int(input(f"{number1} {op} {number2} = "))
      result=0
      match(op):
         case '+':
            result=number1+number2
         case '-':
            result=number1-number2
         case '*':
            result=number1*number2
         case '//':
            result=number1//number2
         case '%':
            result=number1%number2
         case _:
            print("Something Went Wrong ")
      if userAns==result:
         points+=1
      else:
        print(f"You Miss The Game !!\n with Points : {points}")
        print(f"The Correct Answer Is : {result}")
        break
        
         

number=int(input("Enter Any Number : "))
GameStart(number)
