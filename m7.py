def get_name(q):
    def hello():
        name=q()
        print(f"Привет, {name}!")
    return hello
@get_name
def nam_():

  name = input('Введите имя ')
  return name
nam_()
