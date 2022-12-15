from tkinter import *


def click():
    name=entrnme.get()
    messag=str('Hello, '+name)
    prntnme["text"]=messag





window=Tk()

window.title('Probnik')
window.geometry('450x500')
window['bg']='black'

logo = PhotoImage(file="log1.png")
logoimage=Label(image=logo)
logoimage.place(x=0,y=0)

lbl1=Label(text='Enter yor name:',fg='white',bg='black')
lbl1.place(x=20,y=350)

entrnme=Entry(text="")
entrnme.place(y=350,x=120,width=200,height=20)

prntnme=Message(text="")
prntnme.place(y=390,x=120,width=200,height=50)

btn=Button(text='Click me',bg='white',fg='black',command=click)
btn.place(y=390,x=30,width=80,height=25)

window.mainloop()