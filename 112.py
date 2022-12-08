import csv
file = open('Books.csv', 'a')
book = input('Enter book: ')
author = input('Enter author: ')
year = input('Enter year: ')
newRecord = book + ", " + author + ", " + year + "\n"
file.write(str(newRecord))
file = open('Books.csv', 'r')
print(file.read())