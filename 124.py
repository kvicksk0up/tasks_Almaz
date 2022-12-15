from tkinter import *


def privet():
    msg = Label(window, text='Hello'+', '+ entry_box.get()+'!')
    msg.place(x=30, y=170)
    window['bg']='pink'
    button['bg']='violet'
    button['fg']='white'
    msg['bg']='red'
    lbl1['bg']='pink'


window = Tk()
window.geometry('300x200')
window.resizable(False,False)
lbl1=Label(text='Enter yor name:')
lbl1.place(x=110, y=20)
entry_box = Entry()
name=entry_box
entry_box.place(x=90,y= 50 )
button=Button(bg='black',fg='white',text='Click me!', command=privet)
button.place(x=120,y=100)



window.mainloop()


