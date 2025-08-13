class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # gizli atribut

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
acc = BankAccount("Aynur", 200)
acc.deposit(120)
acc.withdraw(50)
print(acc.get_balance())  