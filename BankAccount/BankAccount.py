class BankAccount:
    #used encapsulation for denying direct access to the _balance info
    def __init__(self, balance = 0):
        self._balance = balance


    def deposit(self,amount):
        
        if amount <= 0:
            print(" deposit amount must be positive")
            return
        self._balance += amount


    def withdraw(self,amount):
        if amount <= 0:
            print(" withdrawal amount must be positive")
            return
        if amount > self._balance:
            print("Insufficient funds.")
            return
        self._balance -= amount
    
    def check_balance(self):
        return self._balance

    def __str__(self):
        return f"BankAccount balance: {self._balance}"