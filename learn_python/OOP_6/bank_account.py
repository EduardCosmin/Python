#Bank account

#Create a bank account with two attributes:
#   -owner
#   -balance
#and two methods
#   -deposit
#   -withdraw

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Welcome to the Royal Bank\nAccount owner: {self.owner}\nAccount balance: RON {self.balance}"

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f'Added RON {deposit_amount} to the balance.')

    def withdrawal(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance = self.balance-withdrawal_amount #substract the value that you withdraw
            print (f"Transaction approved, you withdraw RON {withdrawal_amount}!")
        else:
            print (f"You tried to withdraw RON {withdrawal_amount}, but your current balance is RON {self.balance}!\nFunds Unavailable!")



acct1=Account('Diana', 500)
print(acct1)
print('The current account owner is {}.'.format(acct1.owner))
print('The current balance for {} is RON {}.'.format(acct1.owner, acct1.balance))
acct1.deposit(100)
print(f"Your current balance is: RON {acct1.balance}.")
acct1.withdrawal(300)
print(f"Your current balance is RON {acct1.balance}")
acct1.withdrawal(400)