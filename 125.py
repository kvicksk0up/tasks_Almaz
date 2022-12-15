from tkinter import *
import random

def lesgo():
    i = random.randint(1, 6)
    b = random.randint(1, 6)
    msg1=Label(window,text=i )
    msg1.place(x=120, y=10)
    msg2=Label(text=b)
    msg2.place(x=120, y=50)
    lbl1=Label(window,text='Your num:')
    lbl1.place(x=40, y=10)
    lbl2 = Label(window, text='Bots num:')
    lbl2.place(x=40, y=50)

    if i>b:
        msg3=Label(text='You win!')
        msg3.place(x=120, y=150)

    elif i==b:
        msg5 = Label(text='Draw!')
        msg5.place(x=120, y=150)

    else:
        msg4=Label(text='You lose!')
        msg4.place(x=120, y=150)



window=Tk()
window.geometry('300x200')
window.resizable(False,False)
button=Button(text='Click me!', command=lesgo)
button.place(x=120,y=100)


window.mainloop()
