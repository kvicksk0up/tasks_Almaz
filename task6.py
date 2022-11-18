def count():
    i=0
    res2 = 0
    res1 = 0
    while i<10:
        i+=1
        if i%2==0:
            res2+=1
        else:
            res1+=1
    print(f'Четных чисел: {res2}, нечетных: {res1}')
count()

