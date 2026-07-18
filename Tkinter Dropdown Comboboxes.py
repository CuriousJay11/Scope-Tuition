from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Select Course")

course = ttk.Combobox(window)
course["values"] = ('1','2','3','4','5','6','7','8','9','10')
course.pack()

def show():
    print(course.get())

Button(window, text="Select Course", command=show).pack(pady=10)

window.mainloop()
