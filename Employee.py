from abc import ABC ,abstractmethod

class employee(ABC):
    company="NASA Company"
    def __init__(self,name,dep,accNo,amt,stipend):
        self.dep=dep
        self.accNo=accNo
        self.amount=amt 
        self.name=name
        self.stipend=stipend

    @abstractmethod
    def empNature(self,nature):
        pass
    @abstractmethod
    def empStipend(self):
        pass        
    def depositSalary(self,amt):
        self.amount+=amt
    
    @abstractmethod
    def empDetails(self):
       pass

class fullTimeEmployee(employee):
    def empNature(self, nature):
        print(f"{self.name} {nature}")
    def empStipend(self):
        print(f"TOtal Stipend ={self.stipend}")
    def empDetails(self):
        print(f"Employee Name = {self.name}")
        print(f"His Account Number ={self.accNo}")
        print(f"Department = {self.dep}")
        print(f"Total Amount ={self.amount}")
        print(f"Stipend = {self.stipend}")

class partTime(employee):
    def empNature(self, nature):
        print(f"{self.name} {nature}")
    def empStipend(self):
        print(f"TOtal Stipend ={self.stipend}")
    def empDetails(self):
        print(f"Employee Name = {self.name}")
        print(f"His Account Number ={self.accNo}")
        print(f"Department = {self.dep}")
        print(f"Total Amount ={self.amount}")
        print(f"Stipend = {self.stipend}")
    

ram=fullTimeEmployee("Ram","IT Sector",12345,2000,120)
ram.empNature("ram is a good boy")
ram.empStipend()
ram.depositSalary(200)
ram.empDetails()

shyam=fullTimeEmployee("Shyam","Banking Sector",9800001,4000,130)
shyam.empNature("shyam is a good boy")
shyam.empStipend()
shyam.empDetails()