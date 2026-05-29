from tkinter import *

window=Tk()

window.title("Transparent Window") 
window.geometry("400x300") 

window.attributes("-alpha",0.8)

window.mainloop()