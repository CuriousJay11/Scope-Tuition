class BankAccount:
    def __init__(self):
        self.acc_num = 0
        self.acc_holder = ""
        self.balance = 0

    
    def create_account(self):
        self.acc_num = int(input("Enter Acc No: "))
        self.acc_holder = input("Enter Acc Holder Name: ")
        self.balance = input("Enter Opening Balance: ")

    
    def deposit(self):
        amount = input("Enter Deposit Amount: ")
        self.balance += amount
        print("Amount Deposited Successfully.")

    
    def withdraw(self):
        amount = input("Enter Withdraw Amount: ")
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

   
    def check_balance(self):
        print("Current Balance:", self.balance)

    
    def display_details(self):
        print("\n- Account Details -")
        print("Account No   :", self.acc_num)
        print("Holder Name  :", self.acc_holder)
        print("Balance      :", self.balance)



account = BankAccount()
account.create_account()

while True:
    print("\n====== BANK MENU ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        account.deposit()

    elif choice == 2:
        account.withdraw()

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.display_details()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")