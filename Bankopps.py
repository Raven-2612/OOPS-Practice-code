
class BankAccount:

    def __init__(self,holder_name,balance=0):
        self.holder_name=holder_name
        self.balance=balance

    def deposite(self,amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
        

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficent Balance")
        else:
            self.balance-=amount

    def show_balance(self):
        print(f"{self.holder_name}'s balance: {self.balance}") 


acc = BankAccount("Arun", 1000)
acc.deposite(500)
acc.withdraw(2000)  
acc.withdraw(300)
acc.deposite(-50)     
acc.show_balance()   
