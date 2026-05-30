from tkinter import *

root = Tk()

choice = StringVar()

Radiobutton(root, text="male", variable=choice, value="male").pack()
Radiobutton(root, text="female", variable=choice, value="female").pack()

def show():
    print(choice.get())

Button(root, text="submit", command=show).pack()

root.mainloop()