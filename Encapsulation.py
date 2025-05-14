# account_class.py

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # Public attribute
        self._balance = balance   # Protected attribute (by convention)
        self.__pin = "1234"       # Private attribute (name mangled)

    # Public method
    def show_balance(self):
        print(f"{self.owner}'s balance is: ${self._balance}")

    # Protected method (convention: not to be accessed directly)
    def _update_balance(self, amount):
        self._balance += amount

    # Private method
    def __get_pin(self):
        return self.__pin

# Create an account object
account = BankAccount("Zainab", 500)

# Accessing public member
account.show_balance()

# Accessing protected member (not recommended, but possible)
print("Accessing protected _balance:", account._balance)

# Trying to access private member directly (will fail)
try:
    print("PIN:", account.__pin)
except AttributeError:
    print("Cannot access private attribute '__pin' directly.")

# Accessing private attribute via name mangling (not recommended)
print("Accessing mangled private attribute:", account._BankAccount__pin)

