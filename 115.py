import csv

file = list(csv.reader(open('Books.csv')))
tmp = []
for row in file:
    tmp.append(row)

x = 0
n = 0
for row in tmp:

   print(f'row: {n} {tmp[x]}')
   x+=1
   n+=1
