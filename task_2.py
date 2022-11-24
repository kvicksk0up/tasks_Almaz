class  Queue:

    def __init__(self,inside=['Ver','Alm','Adl']):
        self.inside=inside

    def __str__(self,i=0):
        lst = []
        while i!=len(self.inside):
            x=f'{self.inside[i]}=>'
            i += 1
            lst.append(x)
        return ''.join(lst)


    def __add__(self, other):
        self.inside.append(other)

    def __isub__(self, other):

        if len(self.inside)==0:
            print('Очередь пустая')

        else:
            self.inside.remove(other)
        return self

b=Queue()
b+'Ser'
b-='Alm'
b-='Ver'
b-='Adl'
b-='Ser'
b+'1'
b+'12'
print(b)



