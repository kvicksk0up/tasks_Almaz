file = open("Name.txt", "r")
print(file.read())
file.close()
file=open("Name.txt", "r")
dn = input("Enter a name from the list:")
dn = dn + "\n"
for row in file:
    if row != dn:
        file = open("Name2.txt", "a")
        newrecord = row
        file.write(newrecord)
        file.close()
    file.close()

