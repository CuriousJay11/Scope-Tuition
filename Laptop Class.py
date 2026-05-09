class Laptops():
    Screen=1
    Keyboard=1
    def __init__ (self,colours,brands,sizes,graphics,usage):
        self.colour = colours
        self.brands = brands
        self.sizes = sizes
        self.graphics = graphics
        self.usage = usage
    
    def Watching(self):
        ("Lets watch something")

    def Gaming(self):
        ("Lets Play Some Games")

Object1 = Laptops("Red","Lenovo Legion","32x16","Radeon","Gaming")
Object2 = Laptops("Blue","HP Pavillion","34x18","NVIDIA GeForceRTX","MutliUse")
Object3 = Laptops("White","MacBook Pro","24x18","M4 Series","Studying")

print(Object1.graphics,Object1.colour,Object1.sizes,Object1.usage,Object1.brands)
print(Object2.graphics,Object2.colour,Object2.sizes,Object2.usage,Object2.brands)