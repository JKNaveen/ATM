class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance"

    def check_balance(self):
        return self.balance

    def display_info(self, show_balance=True):
        info = f"Account Number: {self.account_number}"
        if show_balance:
            info += f"\nBalance: {self.balance}"
        return info

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN successfully changed"

    def transfer(self, amount, target_account):
        if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            return f"Transferred {amount} to account {target_account.account_number}. New balance: {self.balance}"
        else:
            return "Insufficient balance for transfer"

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate, pin):
        super().__init__(account_number, balance, pin)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        return f"Added interest {interest}. New balance: {self.balance}"

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, pin):
        super().__init__(account_number, balance, interest_rate, pin)

    def exclusive_benefit(self):
        return "Exclusive benefit for premium savings account holders."

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit, pin):
        super().__init__(account_number, balance, pin)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance and overdraft limit"

class OnlineBanking:
    def online_deposit(self, amount):
        return self.deposit(amount)

    def online_withdraw(self, amount):
        return self.withdraw(amount)

class MobileBanking:
    def mobile_deposit(self, amount):
        return self.deposit(amount)

    def mobile_withdraw(self, amount):
        return self.withdraw(amount)

class HybridBankAccount(Account, OnlineBanking, MobileBanking):
    def __init__(self, account_number, balance, pin):
        super().__init__(account_number, balance, pin)
