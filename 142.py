import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)
    print()
    
location = input("Enter a place of birth: ")
print()
cursor.execute("""SELECT Books.Title,  Books.DatePublished, Books.AuthorFROM Books,Authors WHERE Authors.Name = Books.Author AND Authors.PlaceofBirth = ? """,[location])
for x in cursor.fetchall():
    print(x)

db.close()
