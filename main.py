from banking import SavingsAccount, PremiumSavingsAccount, CheckingAccount, HybridBankAccount
from db_connection import create_table
from db_operations import get_account, create_account, update_account_balance, change_pin, transfer_funds

def atm_interface(account):
    while True:
        print("\nWelcome to the ATM machine.")
        pin = int(input("Please enter your PIN: "))

        if pin != account['pin']:
            print("Incorrect PIN. Please try again.")
            continue

        print("\nMenu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Transfer Funds")
        print("6. Mobile Deposit")
        print("7. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            print("Current balance:", account['balance'])

        elif option == 2:
            amount = float(input("Enter the amount to withdraw: "))
            if account['balance'] >= amount:
                account['balance'] -= amount
                update_account_balance(account['account_number'], account['balance'])
                print(f"Withdrew {amount}. New balance: {account['balance']}")
            else:
                print("Insufficient balance")

        elif option == 3:
            amount = float(input("Enter the amount to deposit: "))
            account['balance'] += amount
            update_account_balance(account['account_number'], account['balance'])
            print(f"Deposited {amount}. New balance: {account['balance']}")

        elif option == 4:
            new_pin = int(input("Enter your new PIN: "))
            change_pin(account['account_number'], new_pin)
            account['pin'] = new_pin
            print("PIN successfully changed")

        elif option == 5:
            target_account_number = input("Enter the target account number: ")
            target_account = get_account(target_account_number)
            if target_account:
                amount = float(input("Enter the amount to transfer: "))
                if account['balance'] >= amount:
                    account['balance'] -= amount
                    target_account['balance'] += amount
                    update_account_balance(account['account_number'], account['balance'])
                    update_account_balance(target_account_number, target_account['balance'])
                    print(f"Transferred {amount} to account {target_account_number}. New balance: {account['balance']}")
                else:
                    print("Insufficient balance for transfer")
            else:
                print("Target account not found.")

        elif option == 6:
            amount = float(input("Enter the amount to deposit via mobile: "))
            account['balance'] += amount
            update_account_balance(account['account_number'], account['balance'])
            print(f"Mobile deposit of {amount}. New balance: {account['balance']}")

        elif option == 7:
            print("Thank you for using the ATM machine.")
            break

        else:
            print("Invalid option. Please try again.")
def main():
    create_table()

    print("Welcome to the ATM system!")
    user_choice = input("Are you a new user or existing user? (new/existing): ").strip().lower()

    if user_choice == "new":
        acc_num = input("Enter a new 10-digit account number: ").strip()
        balance = float(input("Enter initial deposit amount: "))
        pin = int(input("Set a 4-digit PIN: "))
        acc_type = input("Enter account type (Savings/Checking): ").strip()

        if acc_type.lower() == "savings":
            interest_rate = float(input("Enter interest rate (%): "))
            create_account(acc_num, balance, pin, "Savings", interest_rate=interest_rate)
        elif acc_type.lower() == "checking":
            overdraft_limit = float(input("Enter overdraft limit: "))
            create_account(acc_num, balance, pin, "Checking", overdraft_limit=overdraft_limit)
        else:
            print("Invalid account type.")
            return

    elif user_choice == "existing":
        acc_num = input("Enter your account number: ").strip()
        pin = int(input("Enter your PIN: "))
        account = get_account(acc_num)

        if account and account['pin'] == pin:
            atm_interface(account)
        else:
            print("Invalid account number or PIN.")
            return

    else:
        print("Invalid option selected.")
        return

if __name__ == "__main__":
    main()
