class Cat:

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        return "Meow"

    def mur(self):
        return "Мur"

    def sleep(self):
        return "Zzz..."

tom = Cat("Tom","Orange",10)

print(tom.name, tom.color, tom.age)
print(tom.mur())
print(tom.sleep())
print(tom.meow())