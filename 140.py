import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor=db.cursor()

print('Main Menu''\n''\n'
'1) View phone book''\n'
'2) Add to phone book''\n'
'3) Search for surname''\n'
'4) Delete person from phone book''\n'
'5) Quit''\n')



num=int(input('Enter your selection: '))



if num==1:
    cursor.execute("SELECT * FROM Names")
    for i in cursor.fetchall():
        print(i)

elif num==2:
    newID = input("Enter ID number: ")
    newName = input("Enter name: ")
    newSurn = input("Enter Surname: ")
    newPhone= input("Enter Phonenumber: ")
    cursor.execute("""INSERT INTO Names(ID, First_name, Surname, Phone_number)
    VALUES(?, ?, ?, ?)""", (newID,newName,newSurn,newPhone))
    db.commit()

elif num==3:
    search = input("Enter a Surname: ")
    cursor.execute("SELECT * FROM Names WHERE Surname=?", [search])
    for x in cursor.fetchall():
        print(x)

elif num==4:
    ser=int(input("Which ID should to delete: "))
    cursor.execute("DELETE FROM  Names WHERE ID=?",[ser])
    db.commit()

elif num==5:
    db.close()

else:
    print("Incorrect selection entered")

db.close()











