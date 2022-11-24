class Batary:
    def __init__(self):
        self.capacity=[]

    def load(self):
        a = ')'
        if len(self.capacity)>=5:
            print('Батарея заряжена')
        else:
            self.capacity.append(a)


    def unload(self):
        a=')'
        if a not in self.capacity:
            print('Батарея разряжена')
        else:
            self.capacity.pop()

    def __str__(self):
        return f'power: {self.capacity}'

n=Batary()
n.load()
n.load()
n.load()
n.load()
n.load()
n.unload()
print(n)
