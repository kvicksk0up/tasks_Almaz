from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self,size):
        self.size=size

    def __add__(self, other):
        return f'Общийрасход ткани на костюм с пальто:{self.size/6.5+0.5+other.size*2+0.3} '

    @abstractmethod
    def my_method(self):
        pass

class Coat(Clothes):

    @property
    def expenses(self):
        return f'Расход ткани на пальто: {self.size / 6.5 + 0.5}'

    def my_method(self):
        pass

class Costume(Clothes):

    @property
    def expenses(self):
        return f'Расход ткани на костюм: {self.size*2+0.3}'

    def my_method(self):
        pass

a=Coat(20)
b=Costume(30)
print(a.expenses)
print(b.expenses)
print(a+b)

