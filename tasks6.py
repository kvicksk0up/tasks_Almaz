from string import ascii_lowercase
a=ascii_lowercase
gen=(i for i in a)
alph={key : value for key,value in zip(range(1,100), gen)}
print(alph)