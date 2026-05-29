from tkinter import *

window=Tk()

window.title("Window") 
window.geometry("1000x1000") 
window.configure(bg="Lightblue")

#window Resize Disable

window.resizable(False,False)

#window icon
#window.iconbitmap("icon.ico")

#Transparancy
window.attributes("-alpha",0.5)

Label(window,text= "Weather is sunny!",font=("EB Garmond",20),bg='white',fg='black').pack(padx=400,pady=200)#50 pixel from above and side


window.mainloop()