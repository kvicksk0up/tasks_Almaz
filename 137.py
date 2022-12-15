from tkinter import *

def add_to_list():
    name = namebox.get()
    namebox.delete(0, END)
    genderselection = gender.get()
    gender.set("M/G")
    newdata = name + ", " + genderselection + "\n"
    name_list.insert(END, newdata)
    file = open("names.txt", "a")
    file.write(newdata)
    file.close()

def print_list():
    file = open("names.txt", "r")
    print(file.read())


window = Tk()
window.title("People list")
window.geometry("400x400")
namelbl = Label(text = "Enter their name:")
namelbl.place(x = 50, y = 50, width = 100, height = 25)
namebox = Entry(text = "")
namebox.place(x = 150, y = 50, width = 150, height = 25)
genderlbl = Label(text = "Select Gender")
genderlbl.place(x = 50, y = 100, width = 100, height = 25)
gender = StringVar(window)
gender.set("M/G")
gendermenu = OptionMenu(window, gender, "Men", "Girl")
gendermenu.place(x = 150, y = 100)
name_list = Listbox()
name_list.place(x = 150, y = 150, width = 150, height = 100)
addbtn = Button(text = "Add to List", command = add_to_list)
addbtn.place(x = 50, y = 300, width = 100, height = 25)
printlst = Button(text = "Print List", command = print_list)
printlst.place(x = 175, y = 300, width = 100, height = 25)


window.mainloop()