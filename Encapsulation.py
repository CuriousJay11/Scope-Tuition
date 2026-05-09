class BankAccount:

    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

        else:
            print("Deposit amount must be positive.")


    def withdrawal(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"New balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance
        
my_account = BankAccount(1000)
my_account.deposit(200)
my_account.withdrawal(500)

print(f"current balance: {my_account.get_balance()}")



