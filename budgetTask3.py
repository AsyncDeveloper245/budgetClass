class BudgetException(Exception):
    pass


class Budget:
    """
    Budget class with Food, clothing ,Entertainment categories


    Withdraw(category,amount)--> To withdraw from a category you specify the category as 1st argument followed
        by the amount
        if amount is > A BudgetException is raised.

    Deposit(category,amount) --> To deposit to a particular category, you input the category as 1st argument
        to the deposit function followed by the amount to be deposited

    Transfer(sender,receiver,amount) --> To transfer money between categories you specify the sending category as 1st
        argument, the receiving category as the 2nd argument and the amount being transferred as 3rd argument.
    """

    def __init__(self, food, clothing, entertainment):
        if food:
            self.food = dict()
            self.food['balance'] = 0
        if clothing:
            self.clothing = dict()
            self.clothing['balance'] = 0

        if entertainment:
            self.entertainment = dict()
            self.entertainment['balance'] = 0

    def compute_balance(self, category):
        category = category.title()
        if category == 'Food':
            return self.food['balance']

        if category == 'Clothing':
            return self.clothing['balance']

        if category == 'Entertainment':
            return self.entertainment['balance']

        else:
            raise BudgetException

    def withdraw(self, category, amount):
        try:
            category = category.title()
            if category == 'Food':
                if amount > self.food['balance']:
                    raise BudgetException
                self.food['balance'] -= amount

            if category == 'Clothing':
                if amount > self.clothing['balance']:
                    raise BudgetException
                self.clothing['balance'] -= amount

            if category == 'Entertainment':
                if amount > self.entertainment['balance']:
                    raise BudgetException
                self.entertainment['balance'] -= amount

        except BudgetException:
            print('Insufficient Balance')

    def transfer(self, sender, receiver, amount):
        sender = sender.title()
        receiver = receiver.title()
        try:

            if sender == 'Food' and receiver == 'Clothing':
                if amount > self.food['balance']:
                    raise BudgetException
                self.food['balance'] -= amount
                self.clothing['balance'] += amount

            if sender == 'Food' and receiver == 'Entertainment':
                if amount > self.food['balance']:
                    raise BudgetException
                self.food['balance'] -= amount
                self.entertainment['balance'] += amount

            if sender == 'Clothing' and receiver == 'Food':
                if amount > self.clothing['balance']:
                    raise BudgetException
                self.clothing['balance'] -= amount
                self.food['balance'] += amount

            if sender == 'Clothing' and receiver == 'Entertainment':
                if amount > self.clothing['balance']:
                    raise BudgetException
                self.clothing['balance'] -= amount
                self.entertainment['balance'] += amount

            if sender == 'Entertainment' and receiver == 'Food':
                if amount > self.entertainment['balance']:
                    raise BudgetException
                self.entertainment['balance'] -= amount
                self.food['balance'] += amount

            if sender == 'Entertainment' and receiver == 'Clothing':
                if amount > self.entertainment['balance']:
                    raise BudgetException
                self.entertainment['balance'] -= amount
                self.clothing['balance'] += amount

        except BudgetException:
            print("Insufficient Balance")

    def deposit(self, category, amount):
        category = category.title()
        if category == 'Food':
            self.food['balance'] += amount

        if category == 'Clothing':
            self.clothing['balance'] += amount

        if category == 'Entertainment':
            self.entertainment['balance'] += amount

    def __str__(self):
        return f"Budget class Food-> {self.food} - Clothing-> {self.clothing} - Entertainment-> {self.entertainment}"


newbudget = Budget('food', 'clothing', 'entertainment')

newbudget.deposit('food', 30000)

print(newbudget.compute_balance('food'))
newbudget.transfer('food', 'clothing', 5000)
newbudget.transfer('food', 'entertainment', 700000)
print(newbudget.compute_balance('clothing'))
print(newbudget)
newbudget.withdraw('entertainment', 1250)
print(newbudget)
