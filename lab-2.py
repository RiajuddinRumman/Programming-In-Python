class BankAccount :
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def display(self):
        print(self.name)
        print(self.balance)


account = BankAccount("John",100)
account.deposit(50)
account.withdraw(20)
account.display()