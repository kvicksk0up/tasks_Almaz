class Father:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Child(Father):

    def __init__(self, patronim,name,surname):
        super(Child, self).__init__(name, surname)
        self.patronim = patronim

child = Child('Ivan','Ivanov', 'Ivanovich')
print(child.name,child.surname,child.patronim)
