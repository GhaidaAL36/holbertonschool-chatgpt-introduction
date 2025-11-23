#!/usr/bin/python3
class Checkbook:
    """
    Class: Checkbook

    Description:
        A simple checkbook class that allows deposits, withdrawals, and balance inquiries.

    Methods:
        deposit(amount): Adds money to the balance.
        withdraw(amount): Removes money from the balance if sufficient funds exist.
        get_balance(): Prints the current balance.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None

        Description:
            Adds the specified amount to the balance and prints the updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None

        Description:
            Subtracts the specified amount from the balance if enough funds are available.
            Prints an error message if funds are insufficient.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Parameters:
            None

        Returns:
            None

        Description:
            Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

