class Bank:
    def __init__(self,name,accountNumber,address,amount):
       self.name=name
       self.address=address
       self.accountNumber=accountNumber
       self.amount=amount

    def showAccountHolder(self):
        print(f"Account Holder = {self.name}")
        print(f"User Address = {self.address}")
        print(f"Total Balance = {self.amount}")
        print(f"Account Number = {self.accountNumber}")

    def ShowActualBalance(self):
        print(f"Acutual Balance is : {self.amount}")

    def Deposit(self,amount):
        self.amount+=amount
        self.ShowActualBalance()

    def withDraw(self,amount):
        self.amount-=amount
        self.ShowActualBalance()

    def updateAccountDetail(self,name,address):
        self.name=name
        self.address=address




name=input("Enter the Account Holder Name : ").capitalize()
address=input("Enter the Address : ")
amount=int(input("Enter the Amount :"))
accountNumber=int(input("Enter the Account Number :"))

user=Bank(name,accountNumber,address,amount)
print("\n\n")
user.showAccountHolder()
user.ShowActualBalance()
amount=int(input("Enter the Amount to Deposit :"))
user.Deposit(amount)
amount=int(input("Enter the Amount To withDraw :"))
user.withDraw(amount)
name=input("Enter the Account Holder Updated  Name : ").capitalize()
user.updateAccountDetail(name,address)

