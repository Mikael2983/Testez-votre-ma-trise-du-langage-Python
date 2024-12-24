class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("le montant du dépôt doit être positif")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance > amount:
                self.balance -= amount
            else:
                print(f"le solde du compte de {self.account_holder} n'est pas suffisant pour ce retrait")
        else:
            print("le montant du retrait doit être positifs")

    def display_balance(self):
        print(f"le solde du compte de {self.account_holder} est de {self.balance}")


account = BankAccount("Harry Potter", 2500)
account.withdraw(3000)
account.display_balance()
account.deposit(1500)
account.display_balance()
account.withdraw(3000)
account.display_balance()
account.deposit(-500)
account.withdraw(-200)