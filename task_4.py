class User:

    def __init__(self,login,password):
        self.login=login
        self.password=password

    def view(self):
        self.f="Я - User. Могу просматривать содержимое"
        return self.f

class Moderator(User):

    def __init__(self,group_id):
        super().__init__('login','password')
        self.group_id=group_id

    def view(self):
        self.f="Я - Moderator. Могу просматривать содержимое"
        return self.f
    def redact(self):
        self.s="Я - Moderator. Могу редактировать содержимое"
        return self.s

i=User('Almaz','123')
not_i=Moderator('id')
print(not_i.view(),not_i.redact())
print(i.view())
