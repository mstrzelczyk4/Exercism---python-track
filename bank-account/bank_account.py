import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.account_open = False
        self.lock = threading.Lock()

    def get_balance(self):
        self.isopen()
        return self.balance

    def open(self):
        if self.account_open:
            raise ValueError("Account already opened")
        self.account_open = True

    def deposit(self, amount):
        self.lock.acquire()
        self.isopen()
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount must be positive")
        self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        self.isopen()
        if self.balance >= amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Amount must not be higher than balance")
        self.lock.release()

    def close(self):
        self.isopen()
        self.account_open = False
        self.balance = 0

    def isopen(self):
        if not self.account_open:
            raise ValueError("Account closed")

