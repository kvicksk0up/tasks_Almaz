def login():
    d = {}
    while True:
        log = input("Введите логин: ")
        password = input("Введите пароль: ")

        pas = d.get(log)
        if pas and pas == password:
            print("Вы успешно авторизовались")
        elif not pas:
            d[log] = password
            print("Регистрация прошла успешно")
        else:
            print("Неверный пароль, доступ запрещен")

login()
