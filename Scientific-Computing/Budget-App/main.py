# Budget App
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, other_category):
        # if self.get_balance() < amount:
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f"Transfer to {other_category.name}")
        other_category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):    
        title = self.name.center(30, '*')  
        result = f"{title}\n"
    
        for item in self.ledger:
            
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}".rjust(7)
            result += f"{description:<23}{amount}\n"

        total = self.get_balance()
        result += f"Total: {total:.2f}"
        return result



# def create_spend_chart(cat_lst):
def create_spend_chart(cat_list):
    width = len(cat_list)
    left_space = "    "
    res_str = ""

    for i in range(100, -1, -10):
        res_str += f"{i}".rjust(3) + "|\n"
        
    res_str += f"{left_space}{'---' * width}"
    
    longest_word = ""
    for item in cat_list:
        if len(item.name) > len(longest_word):
            longest_word = item.name

    ## TODO: loop through longest, stacking vertical names
    return res_str


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
# food.get_balance()
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
auto = Category("Auto")
auto.deposit(1000, 'deposit')
auto.withdraw(500.00, 'test')

auto.withdraw(50, 'Just a long text test here nothing else')
# print(food)
test1 = [food, clothing, auto]

# print(create_spend_chart(["Food", "Clothing", "Auto"]))
print(create_spend_chart(test1))

# Percentage spent by category
# 100|
#  90|
#  80|
#  70|
#  60| o
#  50| o
#  40| o
#  30| o
#  20| o  o
#  10| o  o  o
#   0| o  o  o
#     ----------
#      F  C  A
#      o  l  u
#      o  o  t
#      d  t  o
#         h
#         i
#         n
#         g


# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
# ***********Clothing***********
# Transfer from Food       50.00
#                         -25.55
# Total: 24.55
