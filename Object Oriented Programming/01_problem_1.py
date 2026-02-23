class person:
    def __init__(self,name):
        self.name=name
    
    def show_name(self):
        print("Name:",self.name)
class student(person):
    def greet(self):
        print("Hello ",self.name)

s1=student("Ashish")
s1.show_name()
s1.greet()

