from random import randint

class Box:

    def __init__(self,  name, from_city, target_city):
        self.__name=name
        self.__from_city=from_city
        self.__target_city=target_city
        self.numcode()

    @property
    def name(self):
        return self.__name

    @property
    def from_city(self):
        return self.__from_city

    @property
    def target_city(self):
        return self.__target_city

    @target_city.setter
    def target_city(self,new_target_city):
        self.__target_city=new_target_city
        return self.__target_city

    def __repr__(self):
        return f'{self.postcode}'


    def numcode(self):
       self.__postcode=(f'Серийный номер поссылки: {randint(100,1000)}')

    @property
    def postcode(self):
        return self.__postcode

