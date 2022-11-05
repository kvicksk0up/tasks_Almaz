from random import sample

def countdown():
    s=(sample(range(0, 10), 10))
    print(s)
    s=reversed(s)
    for i in s:
        print(i, end=' ')
        if i==0:
            print(" Пуск " , end=' ')
countdown()
