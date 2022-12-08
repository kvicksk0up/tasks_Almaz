import csv

start=int(input('введите начальный год: '))
end=int(input('Введите крайний год: '))


file = list(csv.reader(open('Books.csv')))
tmp=[]
for row in file:
    tmp.append(row)

x = 1
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x + 1


