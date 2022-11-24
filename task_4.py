from task_3_box import Box

class Truck:

    def __init__(self,name_driver,marka,color_truck):
        self.name_driver = name_driver
        self.marka=marka
        self.color_truck=color_truck
        self.location='' #пункт выдачи
        self.capacity=[]

    def __str__(self):
        pass


    def __add__(self, other):
        self.capacity.append(other)

    def __sub__(self, other):
        self.capacity.remove(other)

box1 = Box('PK', 'Moscow', 'Kazan')
box2 =Box( 'PS 5', 'Anapa', 'Kirov')
box3 =Box( 'Asus', 'Tumen', 'Arsk')

b=Truck('Vsya','Mercedes','blue')
b + box1
b+box2
b+box3
print(b.capacity)
b-box1
print(b.capacity)

