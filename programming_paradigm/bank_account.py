class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available."""
        if amount > self.account_balance:
            return False
        elif amount < 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Print the current account balance formatted to 2 decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")
