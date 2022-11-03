def fib():
    i=0
    lst = [0,1]
    while i<10:
        g = lst[i] + lst[-1]
        i += 1
        lst.append(g)
    return lst
i=iter(fib())
while True:
    print(next(i))
