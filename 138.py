from tkinter import *

def clicked():
    num = selection.get()
    artref = num + ".gif"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()


window = Tk()
window.title("Art")
window.geometry("700x700")
art = PhotoImage(file = "1.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x = 100, y = 0, width = 500, height = 500)
label = Label(text = "Select Art Number: ")
label.place(x = 50, y = 500, width = 100, height = 25)
selection = Entry(text = "")
selection.place(x = 200, y = 500, width = 100, height = 25)

button = Button(text = "See Art", command = clicked)
button.place(x = 150, y = 550, width = 100, height = 25)

window.mainloop()