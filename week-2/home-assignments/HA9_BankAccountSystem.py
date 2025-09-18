class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}\n")


if __name__ == "__main__":
    # Create two BankAccount objects
    account1 = BankAccount("John Doe", 1000.0, "Savings")
    account2 = BankAccount("Jane Smith", 500.0, "Current")

    # Display initial balances
    print("Initial Account Details:")
    account1.display_balance()
    account2.display_balance()

    # Perform deposit operations
    print("Depositing amounts:")
    account1.deposit(200.0)
    account2.deposit(150.0)

    # Display balances after deposit
    print("\nAccount Details After Deposits:")
    account1.display_balance()
    account2.display_balance()

    # Perform withdrawal operations
    print("Withdrawing amounts:")
    account1.withdraw(500.0)
    account2.withdraw(700.0)  # for "Insufficient balance" check

    # Display final balances
    print("\nFinal Account Details:")
    account1.display_balance()
    account2.display_balance()