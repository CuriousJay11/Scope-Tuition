class Vehicle:
    
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} engine started.")

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        print(f"The{self.brand} {self.model} is driving on four wheels")

class Motorcycle(Vehicle):
    def __init__(self,brand,type_moto):
        super().__init__(brand)
        self.type_moto = type_moto

    def ride(self):
        print(f"The{self.brand} {self.type_moto} is driving on two wheels.")

my_car = Car(" Ford","Focus")
my_bike = Motorcycle(" Royal Enfield","Bullet")

my_car.start_engine()
my_bike.start_engine()

my_car.drive()
my_bike.ride()