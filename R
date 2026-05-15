from tkinter import *

window=Tk()

window.title("Password Strength Checker") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="Orange")

Welcome = Label(window,text="Welcome to Jay's RestoBar",bg="White",fg="Black",font=("Cosmic Sans",30))
Welcome.place(x=100,y=100)

Maincourse = Label(window,text="Select Main Course",bg="White",font=("Cosmic Sans",12))
Maincourse.place(x=200,y=200)

Drink = Label(window,text="Select Drink",bg="White",font=("Cosmic Sans",12))
Drink.place(x=200,y=250)

Dessert = Label(window,text="Select Dessert",bg="White",font=("Cosmic Sans",12))
Dessert.place(x=200,y=300)

result = Label(window,fg="Black",font=("Cosmic Sans",30))
result.place(x=200,y=450)

MaincourseSelection = Spinbox(window,bg="Beige",values=("Seafood Predator Pizza","Pepperoni Chickenoni Pizza","Classic Marghrita Pizza","Vegetable Farmhouse"))
MaincourseSelection.place(x=400,y=200)
DrinkSelection = Spinbox(window,bg="Beige",values=("Virgin Mojito","Pacific Blue","Blood Moon Red","Coke","Pepsi","Limeca"))
DrinkSelection.place(x=400,y=250)
DessertSelection = Spinbox(window,bg="Beige",values=("Tres Leches","Choco Monte Ice Cream Sundae","Medusa's Lair","Chcolate Milkshake","Kunafa Pastry","Apple Pie"))
DessertSelection.place(x=400,y=300)

def TotalCost():

    MainCourseOrder = MaincourseSelection.get()
    DrinkOrder = DrinkSelection.get()
    DessertOrder = DessertSelection.get()

    Cost = 0

    # Main Course Prices
    if MainCourseOrder == "Seafood Predator Pizza":
        Cost += 480
    elif MainCourseOrder == "Pepperoni Chickenoni Pizza":
        Cost += 420
    elif MainCourseOrder == "Classic Marghrita Pizza":
        Cost += 350
    elif MainCourseOrder == "Vegetable Farmhouse":
        Cost += 380


    # Drink Prices
    if DrinkOrder == "Virgin Mojito":
        Cost += 120
    elif DrinkOrder == "Pacific Blue":
        Cost += 140
    elif DrinkOrder == "Blood Moon Red":
        Cost += 150
    elif DrinkOrder == "Coke":
        Cost += 60
    elif DrinkOrder == "Pepsi":
        Cost += 60
    elif DrinkOrder == "Limeca":
        Cost += 60


    # Dessert Prices
    if DessertOrder == "Tres Leches":
        Cost += 180
    elif DessertOrder == "Choco Monte Ice Cream Sundae":
        Cost += 200
    elif DessertOrder == "Medusa's Lair":
        Cost += 220
    elif DessertOrder == "Chcolate Milkshake":
        Cost += 150
    elif DessertOrder == "Kunafa Pastry":
        Cost += 210
    elif DessertOrder == "Apple Pie":
        Cost += 170


    result.config(text=Cost)

TotalBill = Button(window,text="Total Bill",bg="White",font=("Cosmic Sans",12),command=TotalCost)
TotalBill.place(x=200,y=400)
window.mainloop()