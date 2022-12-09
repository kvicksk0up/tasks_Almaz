import re

def check():
    try:
        class MyExeption(Exception):
            pass

        lst = input('Введите текст: ')
        if re.search(r'[(!@#$%^&*)]',lst)!=None:
            raise MyExeption
        else:
            print(lst)
    except MyExeption:
        print('Введены недопустимые символы.')
check()









