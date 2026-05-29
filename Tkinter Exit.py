from tkinter import *
from tkinter import messagebox

window=Tk()

window.title("Scanis") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="grey")

def ask():
    result = messagebox.askyesno("Question","Do you want to exit?")
    if result:
        window.destroy()

Exit= Button(window,text="Exit",fg='black',width=30,height=10,command=ask)
Exit.place(x=400,y=300)

window.mainloop()