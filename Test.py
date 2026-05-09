class Account:
    def account_type(self):
        print("The General Account:")

class SavingAccount(Account):
    def account_type(self):
        print("Savings Account:")


# Runtime Polymorphism (Overiding)

acc1 = Account()
acc2 = SavingAccount()

acc1.account_type()
acc2.account_type()

# Method Overloading

def withdraw(amount,limit=None):
    if limit:
        print(f"Withdrawing {amount} with {limit} ")

    else: 
        print(f"ithDrawing {amount}")

withdraw(500)
withdraw(500,1000)


    



    
    