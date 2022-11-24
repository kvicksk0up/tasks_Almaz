def get_password():
    t=input('Введите пароль для шифровки: ')
    t1=hash(t)
    print(t1)
get_password()
