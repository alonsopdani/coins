class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Sorry, not enough funds')

    def statement(self):
        print('Account balance: €{}'.format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return '''{}'s account: Balance €{}'''.format(self.name, self.balance)


x = Current('Dani', 500)

print(x)
x.deposit(300)
print(x.statement())
x.withdraw(800)
print(x.statement())
x.withdraw(800)
print(x.statement())
x.withdraw(800)