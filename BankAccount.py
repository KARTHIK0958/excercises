class BankAccount:
    ROI = 10.5
    def __init__(self):
        self.Name = input("Enter the account holder's name: ")
        self.Amount = float(input("Enter the initial amount in the account: "))

    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.Amount += deposit_amount
        print(f"Amount deposited: {deposit_amount}")
        print(f"Updated balance: {self.Amount}")
    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print(f"Amount withdrawn: {withdraw_amount}")
            print(f"Updated balance: {self.Amount}")
        else:
            print("Insufficient funds to withdraw.")
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated at {BankAccount.ROI}%: {interest}")
        return interest
    def Display(self):
        print(f"Account holder: {self.Name}")
        print(f"Current balance: {self.Amount}")
account1 = BankAccount()  

account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()

print()  

account2 = BankAccount()  
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()
account2.Display()
