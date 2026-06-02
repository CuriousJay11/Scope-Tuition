from tkinter import *

root = Tk()

def show():
    print(entry.get())

entry = Entry(root)
entry.pack()

Button(root, text="Show", command=show).pack()

root.mainloop()