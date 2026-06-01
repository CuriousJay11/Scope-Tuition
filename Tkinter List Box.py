
from tkinter import *

root = Tk()
root.title("Select Course")

listbox = Listbox(root, height=5)

# Insert courses
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")

listbox.pack()


def show():
    print(listbox.get(listbox.curselection()))


Button(root, text="Select Course", command=show).pack(pady=10)


root.mainloop()

