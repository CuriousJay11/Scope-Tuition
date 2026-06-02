import tkinter as tk

# Functions for logic
expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception:
        equation.set(" Error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# GUI Setup
root = tk.Tk()
root.title("Calculator")
equation = tk.StringVar()

# Display
tk.Entry(root, textvariable=equation).grid(columnspan=4)

# Buttons
buttons = [
    '7','8','9','/', '4','5','6','*', '1','2','3','-', 'C','0','=','+'
]
r, c = 1, 0
for btn_text in buttons:
    cmd = lambda x=btn_text: press(x)
    if btn_text == '=': cmd = equalpress
    elif btn_text == 'C': cmd = clear
    
    tk.Button(root, text=btn_text, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()