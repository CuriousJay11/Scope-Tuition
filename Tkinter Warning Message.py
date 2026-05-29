from tkinter import *
from tkinter import messagebox

window=Tk()

window.title("Scanis") #Used to give the title 
window.geometry("300x300") #size of window
window.configure(bg="grey")

def warningmessage():
    messagebox.showinfo("Alert","Stop Virus Is Found, Please RESTART")



button = Button(window,text= "Scan for Virus",font=("EB Garmond",10), width=20,bg= "red", fg="Black",command=warningmessage)
button.place(x=70,y=100)
window.mainloop()

