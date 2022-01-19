class User():
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, value):
        if value < self.balance:
            self.balance -= value
            return f'{self.name} has {self.balance}.'
        else:
            raise ValueError('no money!')

    def check(self, name, value):
        if name.checking_account == True:
            if value < name.balance:
                name.balance -= value
                self.balance += value
                return f'{self.name} has {self.balance} and {name.name} has {name.balance}.'
            else:
                raise ValueError('no money!')
        else:
            raise ValueError('account error!')

    def add_cash(self, value):
        self.balance += value
        return f'{self.name} has {self.balance}.'

Jeff = User('Jeff', 70, False)
Joe = User('Joe', 70, True)

#print(Jeff.withdraw(2))
print(Joe.check(Jeff, 30))
#print(Jeff.add_cash(2))

"""
test.assert_equals(Jeff.withdraw(2), 'Jeff has 68.')
test.assert_equals(Joe.check(Jeff, 50), 'Joe has 120 and Jeff has 18.')
test.assert_equals(Jeff.check(Joe, 80), 'Jeff has 98 and Joe has 40.')
test.assert_equals(Jeff.add_cash(20), 'Jeff has 118.')
"""