def validator():

    try:
        a = float(input('Введите число: '))
        c = a ** 2
    except ValueError:
        c='Введено не число!'
    print(c)
validator()

