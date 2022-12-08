a=int(input('сколько книг хотите внести в таблицу? '))
i=0
file=open('Books.csv','a')
lst=[]

while i<a:
    book = input('Enter book: ')
    author = input('Enter author: ')
    year = input('Enter year: ')
    file.write(book+', '+author+', '+year+'\n')
    i+=1
file.close()

file=open('Books.csv','r')
searchauthor = input("Enter an authors name to search for: ")
file = open("Books.csv", "r")
count = 0

for row in file:
    if searchauthor in str(row):
        print(row)
        count = count + 1
        if count == 0:
            print ("There are no books by that author in this list.")
            file.close()
