import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
ID integer PRIMARY KEY,
First_Name text not null,
Surname text,
Phone_Number text);""")

# cursor.execute("""INSERT INTO Names(ID,First_name,Surname,Phone_number)
#     VALUES("1","Simon","Howeis","01223349752")""")
# db.commit()
#
# cursor.execute("""INSERT INTO Names(ID,First_name,Surname,Phone_number)
#     VALUES("2","KAren","Phillips","01954295773")""")
# db.commit()

cursor.execute(""" INSERT INTO Names(ID, First_name, Surname, Phone_number)
    VALUES("3", "Darren", "Smith", "01583 749012")""")
db.commit()

cursor.execute(""" INSERT INTO Names(ID, First_name, Surname, Phone_number)
    VALUES("4","Anne", "Jones", "01323 567322")""")
db.commit()

cursor.execute(""" INSERT INTO Names(ID, First_name, Surname, Phone_number)
    VALUES("5", "Mark", "Smith", "01223 855534")""")

db.commit()
db.close()





