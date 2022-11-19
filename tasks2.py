from string import ascii_lowercase
i=ascii_lowercase
def alph(i):
    for n in i:
        yield n
a=alph(i)
while True:
    print(next(a))
