class BankAccount():
    def __init__(self,initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")  
        else:
            print("Deposit amount must be positive")

    def withdrawal(self, amount):
        if amount < 0:
            self.balance -= amount
            print(f"Withdrawl Amount {amount}. New balance: {self.balance}")  
        else:
            print("Insufficient Funds")


my_account = BankAccount(1000)
my_account.deposit(200)
my_account.withdrawal(500)





    


    