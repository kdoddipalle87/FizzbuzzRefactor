__author__ = 'kdoddipalle'
class Car:
    hhas_4_tires = True
    has_2_axles = True
    control = "steering wheel"
    def move(self, speed):
        print "Driving upright %s" % speed

    def __init__(self, name, color, make, year):
        self.make = make
        self.name = name
        self.color = color
        self.year = year

class Collectible:
    has_4_tires = True
    has_2_axles = True
    control = "steering wheel"
    def move(self, speed):
        print "Driving sideways %s!" % speed


G37 = Car("G37", "Red", "Infiniti", "2008")
Q50 = Car("Q50", "Black", "Infiniti", "2014")
A7 = Car("A7", "White", "Audi", "2010")
Genesis = Car("Genesis", "Black", "Hyundai", "2012")