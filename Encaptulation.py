class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance
    
account=BankAccount("kamal",5000)
account.deposit(2000)
print(account.get_balance())
        