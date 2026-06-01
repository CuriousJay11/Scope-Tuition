from tkinter import *

root = Tk()
root.title("Coding Course Selection")
root.geometry("300x250")

# Variables for checkbuttons
python_var = IntVar()
java_var = IntVar()
cpp_var = IntVar()

# Checkbuttons
Checkbutton(root, text="Python", variable=python_var).pack(anchor="w")
Checkbutton(root, text="Java", variable=java_var).pack(anchor="w")
Checkbutton(root, text="C++", variable=cpp_var).pack(anchor="w")

# Function to show selected courses
def show():
    selected = []

    if python_var.get():
        selected.append("Python")

    if java_var.get():
        selected.append("Java")

    if cpp_var.get():
        selected.append("C++")

    if selected:
        result_label.config(text="Selected: " + ", ".join(selected))
    else:
        result_label.config(text="No course selected")

# Button
Button(root, text="Show Selection", command=show).pack(pady=10)

# Label to display result
result_label = Label(root, text="")
result_label.pack()

root.mainloop()