# Budget App
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        amount = f"{amount:.2f}"
        self.ledger.append({'amount': amount, 'description': description})
        

    def withdraw(self):
        pass

    def get_balance(self):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass

    

    def __str__(self):
        stars_num = (30 - len(self.name)) // 2
        stars = "*" * stars_num 
        initial_deposit = define_gap("initial deposit", self.ledger[0]['amount'])
        # initial deposit\t{self.ledger[0]['amount']}
        return f"{stars}{self.name}{stars}\n{initial_deposit}"

def define_gap(left, right):
        gap_num = 30 - (len(left) + len(right))
        gap = " " * gap_num
        return f"{left}{gap}{right}"

def create_spend_chart(cat_lst):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
print(food)

# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96