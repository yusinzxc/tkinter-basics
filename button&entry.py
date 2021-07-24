from tkinter import *
from tkinter import ttk


root = Tk()

title = "Loona"
size = "400x400"

e = Entry(root, width=50, fg="red"
)
e.pack()

def result():
	name = f"Hello, {e.get()}"
	label = Label(root, text=name).pack()
	e.select_clear()

button = Button(root, text="submit", command=result).pack()

root.title(title)
root.geometry(size)

root.mainloop()