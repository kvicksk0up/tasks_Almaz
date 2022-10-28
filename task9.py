from random import randint
n = randint(0, 100)
def rand(i):
    a=int(input('Попробуйте угадать число '))
    if a>n:
        print('Вы ввели число чуть больше :)')
    elif a<n:
        print('Вы ввели число чуть меньше :)')
    elif a==n:
        print(f'Поздравляю вы угадали это было чиcло: {a} ')
        return
    if i==1:
        print(f'Вы не угадали, это было число: {n}')
        return
    rand(i-1)
rand(10)