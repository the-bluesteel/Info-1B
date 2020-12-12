class BankAccount:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

    def deposit(self, a):
        self.amount += a

    def withdraw(self, a):
        self.amount -= a

    def __str__(self):
        return f"Le solde du compte bancaire de {self.name} est de {self.amount} euros" if self.amount != 1 \
            else f"Le solde du compte bancaire de {self.name} est de {self.amount} euro"


name = input("Enter a name: ")
amount = int(input("Enter an amount: "))
account = BankAccount(name, amount)
print(account)
w = int(input("Enter how much should be withdrawn: "))
account.withdraw(w)
print(account)
a = int(input("Enter how much should be added: "))
account.deposit(a)
print(account)
