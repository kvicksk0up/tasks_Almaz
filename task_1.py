from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return 'meow'


class Dog(Animal):
    def say(self):
        return 'woof'


cat = Cat('orange', 'danil', '12')
print(cat.name, cat.color, cat.age, cat.say())
