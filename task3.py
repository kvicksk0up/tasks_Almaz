def robot_hello():
    s = []
    while True:
        name=input('Представтесь, пожалуйста ')
        if name in s:
            print(f'Привет, {name}!')
        else:
            print(f'Привет, {name}, рад знакомству!')
            s.append(name)
robot_hello()






