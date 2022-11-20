def cez():
    alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = int(input('Шаг шифровки: '))
    message = input("Сообщение для Дешифровки: ").upper()
    itog = ''
    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit:
             itog += alfavit[new_mesto]
        else:
            itog += i
    print(itog)
cez()

