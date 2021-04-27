

class Category:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.amount += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.amount -= amount
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        return False

    def get_balance(self):
        return self.amount

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False


    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        item = ''
        i = 1
        for i in range (len(self.ledger)):
            item += '{:23.23}'.format(self.ledger[i]["description"]) + '{:>7.2f}'.format(self.ledger[i]["amount"]) + "\n"

        total = self.get_balance()
        output = title + item + "Total: " + str(total)
        return output

    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total


def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    """Create spend chart that takes a list of categories as an argument. It should return
    a string that is a bar chart."""
    title = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        title += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10

    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = ' '*5
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        if(x != len(maxi) - 1):
            nameStr += '\n'

        x_axis += nameStr

    title += dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return title





