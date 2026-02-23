class car:
    def __init__(self,brand,model):
        self.brand=brand 
        self.model=model

    def display(self):
       print("Car Brand:",self.brand)
       print("Car Model:",self.model)
c1=car("BMW","GT 680i")
c2=car("mustang","high model")
c1.display()
c2.display()

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print("Car Brand:",self.brand)
        print("Car Model:",self.model)
c1=car("Audio","R8")
c2=car("BMW","gt 630i")

c1.display()
c2.display()