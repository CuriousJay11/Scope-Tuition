from tkinter import *
from tkinter import messagebox
window=Tk()

window.title("BBALL Academy") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="Lightblue")

def show():
    messagebox.showinfo("",'Your form has been submitted')

heading = Label(window, text= "Register Now For India's #! Basketball Academy Below",font=("EB Garmond",25),bg="white",fg="black")
heading.place(x=100,y=50)
name = Label(window,text= "What is your name",font=("EB Garmond",20),bg='white',fg='black')
name.place(x=100,y=200)
nameentry = Entry(window,width=35,font=("EB Garmond",20),bg="white",fg="Darkblue")
nameentry.place(x=100,y=250)
name = Label(window,text= "Number of Years Experience",font=("EB Garmond",20),bg='white',fg='black')
name.place(x=100,y=300)
nameentry = Entry(window,width=35,font=("EB Garmond",20),bg="white",fg="Darkblue")
nameentry.place(x=100,y=350)
name = Label(window,text= "What is your age",font=("EB Garmond",20),bg='white',fg='black')
name.place(x=100,y=400)
nameentry = Entry(window,width=35,font=("EB Garmond",20),bg="white",fg="Darkblue")
nameentry.place(x=100,y=450)
submitbutton=Button(window,text=("Submit"),bg="red",fg="black",command=show)
submitbutton.place(x=100,y=500)
window.mainloop()

