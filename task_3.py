import re
def find_email():
    str = 'Всем привет! Меня зовут Алексей.Мой email: alex_VB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Mari.na@mail.ru'
    return re.findall('\w+\.?\_?\@\w+\.\w+', str)
print(find_email())
