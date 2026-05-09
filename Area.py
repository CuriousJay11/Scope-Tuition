class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("The area of the square is", self.side * self.side)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("The area of the circle is", 3.14 * self.radius * self.radius)


sq = Square(5)
cr = Circle(5)

for i in (sq, cr):
    i.area()