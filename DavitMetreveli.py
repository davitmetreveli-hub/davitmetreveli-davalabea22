class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"
class House:
    def __init__(self, house_id, price, owner):
        self.house_id = house_id
        self.price = price
        self.owner = owner
        self.status = "selling"
    def sell(self, buyer, loan_amount=0):
        if loan_amount > 0:
            sale_status = "sold bu loan"
            buyer.loan += loan_amount
        else:
            sale_status = "sold"
        self.owner.deposit += self.price
        self.owner = buyer
        self.status = sale_status

