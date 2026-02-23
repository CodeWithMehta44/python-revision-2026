class Vehicle:
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
    def display(self):
        print(f"Brand:{self.Brand} , Model:{self.Model}") 
c1=Vehicle("BMW","GT 680i")
c2=Vehicle("Audio","R8")
c1.display()
c2.display()
class Vehicle:
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
    def display(self):
        print("Brand:",self.Brand)
class Car(Vehicle):
    def show(self):
        print("Model:",self.Model)
c1=Car("BMW","GT 680i")
c2=Car("Audio","R8")
c1.display()
c1.show()
c2.display()
c2.show()

