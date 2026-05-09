from abc import ABC

class Animal(ABC):
    def move(self):
        pass


class Snake(Animal):
    def move(self):
        print("I can slither")


class Lion(Animal):
    def move(self):
        print("I can walk")


class Leopard(Animal):
    def move(self):
        print("I can run very fast")


s = Snake()
s.move()

l = Lion()
l.move()

o = Leopard()
o.move()