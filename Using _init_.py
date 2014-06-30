__author__ = 'kdoddipalle'


class Car:
    def __init__(self):
        print "Car init!"
    def __init__(self, car_name, car_color):
        self.name = car_name
        self.color = car_color
    def move(self, speed):
        print self.name + " is moving " + speed + "!"


G37 = Car("G37", "Red")
print G37.move("fast")
Q50 = Car("Q50", "Black")
print Q50.move("slowly")

