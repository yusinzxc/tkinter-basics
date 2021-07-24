from tkinter import *
from tkinter import ttk


root = Tk()

title = "Loona"
size = "400x400"

color = "red"
def magic():
	label = Label(
	root, text="Suprise", font=("default", 15)).grid(row=0)
	color = "yellow"
	
button = Button(
root, text="Click Me!", padx=100, pady=100, command=magic, bg=color).grid(row=1)

root.title(title)
root.geometry(size)

root.mainloop()