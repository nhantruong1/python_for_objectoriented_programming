
class Circle:
    pai = 3.14
    def __init__(self, radius):
        self.radius = radius
    def circle_circumference(self):
        return 2*Circle.pai*self.radius
    def circle_area(self):
        return Circle.pai*self.radius**2
 

c1 = Circle(7)
c2 = Circle(14)