def calcltr():
    a=input("ведите первое число: ")
    b=input("Введите операцию: ")
    c=input("Введите второе число: ")
    if b=="/" and c=="0":
        print("Делишь на 0, серьезно?")
    else:
        print(eval(f'{a}{b}{c}'))
calcltr()

