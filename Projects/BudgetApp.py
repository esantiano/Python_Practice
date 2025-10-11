class Category:
    def __init__(self,name):
        self.name = name[0].upper() + name[1:]
        self.ledger = []
        self.balance = 0

    def __str__(self):
        result = self.name.center(30,'*') + '\n'
        for transaction in self.ledger:
            result += transaction['description'][:23].ljust(23) + str('{:.2f}'.format(transaction['amount'])).rjust(7) + '\n'
        result += 'Total: ' 
        result += str('{:.2f}'.format(self.balance))
        return result

    def check_funds(self, amount):
        return amount <= self.balance

    def deposit(self, amount, description = ''):
        transaction = {'amount':amount, 'description': description}
        self.ledger.append(transaction)
        self.balance += amount

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.balance -= amount
            transaction = {'amount':-amount,'description':description}
            self.ledger.append(transaction)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self,amount,category):
        if self.withdraw(amount,f'Transfer to {category.name}'):
            category.deposit(amount,f'Transfer from {self.name}')
            return True
        else:
            return False

def create_spend_chart(categories):
    title = 'Percentage spent by category'
    graph_body = ''
    _percentages = []
    _categories = []
    category_names = ''
    # tuples = []
    for category in categories:
        percentage = get_spending_percentage(category)
        _percentages.append(percentage)
        _categories.append(category.name)
    #     tuples.append((category.name, percentage))
    # print(tuples)
    graph_body = create_graph_body(_percentages)
    category_names = create_category_labels(_categories)
    result = f'{title}\n{graph_body} {category_names}'
    return result

def get_spending_percentage(category):
    total_deposited = 0
    total_withdrawn = 0
    for transaction in category.ledger:
        if transaction['amount'] > 0:
            total_deposited += transaction['amount']
        else:
            total_withdrawn += -transaction['amount']
    return round(100*(total_withdrawn/total_deposited),-1)

def create_graph_body(percentages):
    graph_body = str()
    for level in range(100,-10,-10):
        graph_body += f'{level}'.rjust(3) + '|'
        for percent in percentages:
            if int(percent) >= level:
                graph_body += ' o '
        graph_body += '\n'
    return graph_body

def create_category_labels(category_names):
    n = len(category_names)
    _max = len(max(category_names, key=len))
    labels = ' '*3 + '-' + '-'*3*n + '\n'
    i = 0
    while i < _max:
        labels += ' '*5
        # print each category vertically
        for j in range(n):
            curr = category_names[j]
            if i > len(curr)-1:
                labels += ' '*3
                continue
            # capitalize first letter
            if i == 0:
                labels += f'{curr[i].upper()}  ' 
            else:
                labels += f'{curr[i]}  '
        labels += '\n'
        i+= 1
    return labels

#region tests
clothes = Category('clothes')
clothes.deposit(100)
# clothes.withdraw(70, 'shirt, pants, shoes, underwear, socks')

food = Category('food')
food.deposit(500)
food.withdraw(45, 'milk, cereal, eggs, bacon, bread')

rent = Category('rent')
rent.deposit(1000)
rent.withdraw(600, 'January')

entertainment = Category('entertainment')
entertainment.deposit(200)
entertainment.withdraw(20,'movies')
# entertainment.transfer(food, 100)

categories = [rent, food, clothes, entertainment]


# print(rent.get_balance())
# print(food.get_balance())
# print(clothes.get_balance())
# print(entertainment.get_balance())
# print(food)
# print(rent)
# print(clothes)
# print(entertainment)
# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)

print(create_spend_chart(categories))
#endregion

#region chatgpt solution
def create_spend_chart(categories):
    import math

    # 1) compute spent for each category (sum of negative ledger amounts as positive numbers)
    spent = []
    for c in categories:
        total = 0
        for t in c.ledger:
            if t['amount'] < 0:
                total += -t['amount']
        spent.append(total)

    total_spent = sum(spent)
    if total_spent == 0:
        percentages = [0 for _ in spent]
    else:
        # 2) percent for each category rounded down to nearest 10
        percentages = [math.floor((s / total_spent) * 100 / 10) * 10 for s in spent]

    # 3) build chart header and body
    lines = []
    lines.append("Percentage spent by category")

    # rows 100..0
    for level in range(100, -10, -10):
        row = str(level).rjust(3) + "|"
        for p in percentages:
            if p >= level:
                row += " o "
            else:
                row += "   "
        # add one extra space so the total line width matches dashes/labels below
        row += " "
        lines.append(row)

    # horizontal line: 4 leading spaces, then 3*len(categories)+1 dashes
    dash_count = 3 * len(categories) + 1
    lines.append("    " + "-" * dash_count)

    # category labels vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        row = "     "  # 5 spaces (4 from axis + 1)
        for c in categories:
            if i < len(c.name):
                row += c.name[i] + "  "
            else:
                row += "   "
        lines.append(row)

    # join and return (no trailing newline)
    return "\n".join(lines)
#endregion