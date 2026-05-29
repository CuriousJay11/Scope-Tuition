from tkinter import *

window=Tk()

window.title("Window") 
window.geometry("1000x1000") 
window.configure(bg="Lightblue")

Label(window,text= "Buttons",font=("EB Garmond",20),bg='white',fg='black').pack(padx=50,pady=50)

def Hello(name):
    print("Hello" ,name)


Button(window,text="Click Me!",fg='black',command=lambda:Hello("Vijay")).pack(padx=100,pady=100)



window.mainloop()