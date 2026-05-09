class car:
    
    wheels = 4

    def _init_(self, model, make, colour):
      self.model = model
      self.make = make
      self.colour = colour

    def drive(self):
       print(f"The {self.colour} {self.make} {self.model} is driving.")

my_car = car("Ferrari", "LaFerrari", "Red")
your_car = car("Bughati","Enzo","Black")

print(f"My car is a {my_car.colour} {my_car.model}.")
print(f"Your car has {your_car.wheels} wheels.")

my_car.drive()
your_car.drive()

