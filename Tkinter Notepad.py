from tkinter import *

root = Tk()
root.title("Notepad")
root.geometry("1000x1000")
root.configure(bg="red")


scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
text = Text(root,yscrollcommand=scroll.set,bg='Lightblue')
text.pack(fill=BOTH,expand=True)
scroll.config(command=text.yview)

def ClearText():
    text.delete(1.0,END)

delete = Button(root,text='clear',width=10,height=10,command=ClearText)
delete.place(x=900,y=50)


root.mainloop()
    
        