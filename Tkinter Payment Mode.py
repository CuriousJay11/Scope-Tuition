from tkinter import *

root = Tk()
root.title("Payment Selection") 
root.geometry("1000x1000") 
root.configure(bg="Lightblue")

choice = StringVar()

Label = Label(root,text="Choose youur payment mode")

Radiobutton(root, text="Cash", variable=choice, value="Cash").pack()
Radiobutton(root, text="Card", variable=choice, value="Card").pack()
Radiobutton(root, text="UPI", variable=choice, value="UPI").pack()
Radiobutton(root, text="Bank Transfer", variable=choice, value="Bank Transfer").pack()

def show():
    print(choice.get())

Button(root, text="Select", command=show).pack()

root.mainloop()