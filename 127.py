from tkinter import *

def add():
    name = enter_name.get()
    list_box.insert(END, name)
    enter_name.delete(0, END)
    enter_name.focus()

def clear():
    enter_name.delete(0, END)
    list_box.delete(0, END)




window=Tk()
window.geometry('700x500')
lbl_add=Label(text='Введите ваше имя: ')
lbl_add.place(x= 60,y= 60)
enter_name=Entry(width=40)
enter_name.place(x=190,y=62)
lbl_list=Label(text='Список имен: ',)
lbl_list.place(x=60, y= 100)
list_box = Listbox()
list_box.place(x= 190,y= 100)
list_box.place()
but1=Button(text='Add name',command=add)
but1.place(x= 100,y= 300)
but2=Button(text='Clear',command=clear)
but2.place(x= 250,y= 300)


window.mainloop()