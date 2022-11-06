from register import *
password=input('Введите пароль: ')
lp={'Миша':'123'}
def login():
    pas = lp.get(username)
    if pas and pas == password:
        print("Доступ разрешён!")
    elif not pas:
        register()
        lp[username] = password
        print('Регистрация прошла успешно!')
    else:
        print('Доступ запрещен!')

def del_user():
    d = input('Введите имя пользователя которого надо удалить: ')
    lp.pop(d)
    print(f'Пользователь {d} удален')
    return d

