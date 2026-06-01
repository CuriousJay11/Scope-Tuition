
from tkinter import *

window = Tk()

menubar = Menu(window)

window.config(menu=menubar)

file_menu = Menu(menubar)

#Addcascade

menubar.add_cascade(label='File',menu=file_menu)

def New():
    print("New file Created")

file_menu.add_command(label = 'New',command=New)
file_menu.add_command(label = 'Edit')
file_menu.add_command(label = 'Copy')
file_menu.add_command(label = 'Save')
file_menu.add_command(label = 'Open')



window.mainloop()