from math import *
def engineer():
    a=int(input("Введите число: "))
    msg=input("Для возведения в степень введите 1, для извлечения квадратного корня 2: ")
    if msg=='1':
        s=int(input("В какую сетепень возведем? "))
        a=pow(a,s)
    elif msg=='2':
        a=sqrt(a)
    print(f'Результат: {a}')
engineer()
