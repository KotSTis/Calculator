from Tkinter import *
top = Tk()
top.wm_title("Calculator")
L1 = Label(top, text="enter expression")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()
