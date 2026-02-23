class Dog:
    def sound(self):
        print("Dog Barks")
    
class Cat:
    def sound(self):
        print("Cow Meows")    #Here sound() is polymorphism and it means same methods but different behaviours.

Animals = [Dog(),Cat()]
for animal in Animals:
    animal.sound()


###Practice...
class Car:
    def start(self):
        print("Car starts with key ")

class Bike:
    def start(self):
        print("Bike strts eith self starts ")

c = Car()
b = Bike()
c.start()
b.start()