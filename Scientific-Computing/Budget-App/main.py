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

    # def define_gap(self, left, right):
    #     gap_num = 30 - (len(left) + len(right))
    #     if gap_num <= 0:
    #         trim_num = 29 - len(right)
    #         left = left[:trim_num]
    #         gap = " "
    #     else:
    #         gap = " " * gap_num
    #     return f"{left}{gap}{right}"

    # def __str__(self):
    #     stars_num = (30 - len(self.name)) // 2
    #     stars = "*" * stars_num 
        
    #     res_str = f"{stars}{self.name}{stars}\n"
        
    #     initial_deposit = self.define_gap("initial deposit", f"{self.ledger[0]['amount']:.2f}")
    #     res_str += initial_deposit +"\n"
        
    #     for item in self.ledger[1:]:
    #         res_str += self.define_gap(item["description"], f"{item['amount']:.2f}") + "\n"
           

    #     total = self.get_balance()
    #     res_str += f"Total: {total}"
    #     return res_str
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



def create_spend_chart(cat_lst):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.get_balance()
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
print(food)

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
