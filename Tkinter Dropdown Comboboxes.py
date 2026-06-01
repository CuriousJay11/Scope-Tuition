from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Select Course")

course = ttk.Combobox(root)
course["values"] = ('Python','Java','C++')
course.pack()

def show():
    print(course.get())

Button(root, text="Select Course", command=show).pack(pady=10)

root.mainloop()
