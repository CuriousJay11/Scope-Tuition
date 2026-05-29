from tkinter import *

window=Tk()

window.title("Colour Buttons") 
window.geometry("1000x1000") 
window.configure(bg="Lightblue")

Label(window,text= "Buttons",font=("EB Garmond",20),bg='white',fg='black').pack(padx=50,pady=50)

def Red():
    print("Red Clicked!")

def Blue():
    print("Blue Clicked!")

def Green():
    print("Green Clicked!")

Button(window,text= "Red",font=("EB Garmond",20),bg='Red',fg='black',command=Red).pack(padx=100,pady=100)
Button(window,text= "Blue",font=("EB Garmond",20),bg='Blue',fg='black',command=Blue).pack(padx=100,pady=100)
Button(window,text= "Green",font=("EB Garmond",20),bg='Green',fg='black',command=Green).pack(padx=100,pady=100)


window.mainloop()