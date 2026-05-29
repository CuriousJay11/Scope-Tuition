from tkinter import *
from tkinter import messagebox

window=Tk()

window.title("Welcome Notification") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="Beige")

def show():
    messagebox.showinfo("Title","Welcome")

Login = Button(window,text="Start",fg='black',width=30,height=10,command=show)
Login.place(x=400,y=300)


window.mainloop()