username = input('Введите ваш логин: ')
un = ['Рейн', 'Боб', 'Бани', 'Миша']
p=False
def checker():
    p=False
    if username not in un:
        p = True
    return p
def validate():
    ns=['#','$','%','&']
    if ns[0] in username:
        return
    elif ns[1] in username:
        return
    elif ns[2] in username:
        return
    elif ns[3] in username:
        return
    else:
        p=True
    return p
def register():
    if checker()==True and validate()==True:
        un.append(username)
        print('Регистрация прошла успешно!')
    else:
        print('Логин не должен содержать "#", "$", "%", "&", либо вы уже зарегистрированы')
