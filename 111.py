import csv
file=open('Books.csv','w')
a='Book, Writer, Year \n'
file.write(str(a))
a='To Kill a Mockingbird, Harper Lee, 1960 \n'
file.write(str(a))
a='A Brief History of Time, Stephen Hawking, 1988 \n'
file.write(str(a))
a='The Great Gatsby F., Scott Fitzgerald, 1922 \n'
file.write(str(a))
a='The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985 \n'
file.write(str(a))
a='Pride and Prejudice, Jan Austen, 1813 \n'
file.write(str(a))
file.close()



