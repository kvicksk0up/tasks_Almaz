class Good:
    def __init__(self,name,price,weight):
        self.name=name
        self.weight=weight
        self.price=price
    def oper(self):
        self.cost=self.weight*self.price
        return self.cost
rez=Good('apple',1234.45,10)
print(rez.oper())


