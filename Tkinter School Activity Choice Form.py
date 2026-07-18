from tkinter import *
from tkinter import messagebox
from tkinter import ttk


window=Tk()

window.title("Activity Sport Form") 
window.geometry("1000x1000") 
window.configure(bg="beige")

def show():
    messagebox.showinfo("",'Your form has been submitted')

heading = Label(window, text= "Sports Choice Form 2026-2027",font=("EB Garmond",25),bg="white",fg="black")
heading.place(x=100,y=50)

heading = Label(window, text= "As part of the program, each student is required to choose one activity from the list of options provided in the form. ",font=("EB Garmond",10),bg="white",fg="black")
heading.place(x=100,y=150)

name = Label(window,text= "Student Full Name",font=("EB Garmond",15),bg='white',fg='black')
name.place(x=100,y=200)
nameentry = Entry(window,width=35,font=("EB Garmond",15),bg="white",fg="black")
nameentry.place(x=100,y=250)
name = Label(window,text= "Grade",font=("EB Garmond",15),bg='white',fg='black')
name.place(x=100,y=300)
course = ttk.Combobox(window)
course["values"] = ('1','2','3','4','5','6','7','8','9','10')
course.place(x=100,y=350)

def show():
    print(course.get())

name = Label(window,text= "Choose ONE sport",font=("EB Garmond",15),bg='white',fg='black')
name.place(x=100,y=400)
nameentry = Entry(window,width=35,font=("EB Garmond",15),bg="white",fg="black")
nameentry.place(x=100,y=450)
submitbutton=Button(window,text=("Submit"),bg="blue",fg="white",command=show)
submitbutton.place(x=100,y=500)





window.mainloop()