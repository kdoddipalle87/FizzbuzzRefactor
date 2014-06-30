__author__ = 'kdoddipalle'


class Car:
    has_4_tires = True
    has_2_axles = True
    control = "steering wheel"

    def move(self, speed):
        print "moving %s!" % speed
        print self.name + " is moving " + speed + "!"

mycar1 = Car()
mycar1.name = "G37"
mycar1.color = "Red"
mycar1.move("fast")

mycar2 = Car()
mycar2.name = "Q50"
mycar2.color = "black"
mycar2.move("Slow")

