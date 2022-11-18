from abc import ABC, abstractmethod

class Stationery(ABC):
    def __init__(self,title):
        self.title=title

    def set_color(self):
        self.set_color='yellow'
        return self.set_color

    @abstractmethod
    def draw(self):
        pass

class Pen(Stationery):
    def color(self):
        super().__init__(title='Pen')
        self.color='blue'

    def draw(self):
        self.f='The pen writes'
        return self.f




class Pencil(Stationery):
    def draw(self):
        self.f='The pencil writes'
        return self.f

class Handle(Stationery):
    def draw(self):
        self.f='The handle writes'
        return self.f


pen=Pen('Pen')
pencil=Pencil('Pencil')
handle=Handle('Handle')
print(pen.title,pen.draw(),pen.set_color())
print(pencil.title,pencil.draw(),pencil.set_color())
print(handle.title,handle.draw(),handle.set_color())
