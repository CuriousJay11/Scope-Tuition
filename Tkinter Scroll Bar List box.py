from tkinter import *

window=Tk()

window.title("Scrollbar") 
window.geometry("250x300") 
window.configure(bg="Lightblue")

scroll = Scrollbar(window,orient=HORIZONTAL)
scroll.pack(side=BOTTOM,fill=X)

Lb = Listbox(window,xscrollcommand=scroll.set)

for i in range(1,51):
    Lb.insert(END,f"Item{i}")
    
Lb.pack(fill=BOTH)

scroll.config(command=Lb.xview)

window.mainloop()


