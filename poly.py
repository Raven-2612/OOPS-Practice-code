class Shape:
    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width

    def area(self):
        return self.lenght * self.width


class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes=[Rectangle(4,5), Circle(3)]

for s in shapes:
    print(f"Area:{s.area():.2f}")