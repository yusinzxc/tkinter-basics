from tkinter import *
from tkinter import ttk


root = Tk()

title = "Loona"
size = "400x400"

label = Label(
root, text="Stan Loona",font=("",20)
).pack()

root.title(title)
root.geometry(size)

root.mainloop()