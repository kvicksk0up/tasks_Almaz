import winsound

class Car:
    def __init__(self,color,marka,kuzov,speed=0):
        self.color=color
        self.marka=marka
        self.kuzov=kuzov
        self.speed=speed
        self.transmission='mechanics'
    def start(self):
        print('Движение, скорость 10 км/ч')
        self.speed=10
    def stop(self):
        self.speed=0
        print('Машина остановилась скорость 0 км/ч')
    def turn(self):
        print('Машина повернула')
    def speed_up(self,i=10):
        self.speed+=i
        print('ускорение, текущая скорость:',self.speed)
        if self.kuzov == 'truck' and self.speed > 60:
            print('Скорость превышена! Разрешенная скорость 60 км/ч')
        elif self.kuzov == 'sedan' and self.speed > 80:
            print('Скорость превышена! Разрешенная скорость 80 км/ч')
    def speed_down(self,i=10):
        self.speed-=i
        print('снижение скорости, текущая скорость:', self.speed)
        if self.kuzov == 'truck' and self.speed > 60:
            print('Скорость превышена! Разрешенная скорость 60 км/ч')
        elif self.kuzov == 'sedan' and self.speed > 80:
            print('Скорость превышена! Разрешенная скорость 80 км/ч')

    def beep(self):
        beep=winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
        return beep
car=Car("orange",'mazda','sedan','mechanics')
car.start()
car.speed_up(100)
car.stop()
car.beep()
car1=Car('black','Ford','truck','auto')
car1.start()
car1.speed_up(60)
car1.speed_down(20)
car1.beep()





