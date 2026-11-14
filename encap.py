
class BankAccount:

    def __init__(self,holder_name,balance=0):
        self.holder_name=holder_name
        self.__balance=balance

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.__balance += amount
        

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance-=amount

    def show_balance(self):
        print(f"{self.holder_name}'s balance: {self.__balance}") 


    def get_balance(self):
        return self.__balance


acc = BankAccount("Arun", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())   
print(acc._BankAccount__balance)   
     
