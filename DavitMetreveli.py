class Person:
    def __init__(self, name, depostiy=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
    def __str__(self):
        return f"nameis {self.name}, deposit {self.deposit}, loanl {self.loan}"
class House:
    def __init__(self, houseid, price, owner):
        self.houseid = houseid
        self.price = price
        self.owner = owner
        self.status = "selling"
    def sell(self, buyer, loanamount=0):
        if loanamount >0:
            salestatus = "sold bu loan"
            buyer.loan += loanamount
        else:
            salestatus = "sold"
        self.owner.deposit += self.price
        self.owner =buyer
        self.status =salestatus

