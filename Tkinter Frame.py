from tkinter import *
window=Tk()

frame = Frame(window,bg='red').pack(padx =200, pady=200)

name1 = Label(window,text= "Inside Frame",font=("EB Garmond",20),bg='pink',fg='black')
name1.place(x=100,y=200)

Button = Button(window,text="Click! Fast",fg='red',width=30,height=10)
Button.place(x=300,y=300)

window.mainloop()

