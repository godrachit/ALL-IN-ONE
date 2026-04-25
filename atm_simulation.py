class Account:
    def __init__(self):
        self.balance = 1000
        self.transactions = []

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount


def add_transaction(account, message):
    account.transactions.append(message)


def show_statement(account):
    if not account.transactions:
        print("No transactions yet.")
    else:
        print("\n--- Statement ---")
        for t in account.transactions:
            print(t)


def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account.update_balance(amount)
    add_transaction(account, f"Deposited: ₹{amount}")
    print("Deposit successful!")


def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount > account.get_balance():
        print("Insufficient balance!")
    else:
        account.update_balance(-amount)
        add_transaction(account, f"Withdrawn: ₹{amount}")
        print("Withdrawal successful!")


def check_balance(account):
    print(f"Current Balance: ₹{account.get_balance()}")


def main():
    account = Account()

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance(account)

        elif choice == "2":
            deposit(account)

        elif choice == "3":
            withdraw(account)

        elif choice == "4":
            show_statement(account)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()