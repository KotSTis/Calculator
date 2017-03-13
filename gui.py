from Tkinter import *
import proccessline

master = Tk()

e = Entry(master)
e.pack()
e.focus_set()

def callback():
    print main(e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

master.mainloop()
