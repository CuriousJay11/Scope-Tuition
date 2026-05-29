from tkinter import *

window=Tk()

window.title("Login") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="grey")

name1 = Label(window,text= "Enter Username",font=("EB Garmond",20),bg='white',fg='black')
name1.place(x=100,y=200)

username = Entry(window,width=35,font=("EB Garmond",20),bg="white",fg="Darkblue")
username.place(x=100,y=250)

def login():
    print("Welcome",username.get())

Login = Button(window,text="Login",fg='red',width=30,height=10,command=lambda:login())
Login.place(x=300,y=300)

window.mainloop()