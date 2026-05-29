from tkinter import *

window=Tk()

window.title("Colour Buttons") 
window.geometry("1000x1000") 
window.configure(bg="Lightblue")

def show(num):
    print("No. is",num)

Button(window,text="Click Me!",fg='black',command=lambda:show(1)).pack(padx=100,pady=100)

window.mainloop()