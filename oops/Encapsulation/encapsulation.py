#Unsecure Data.....
class Student:
    def __init__(self,marks):
        self.marks = marks 
    def shows_makrs(self):
        print("marks:",self.marks)
s1 = Student(90)
s1.shows_makrs()

s1.marks = -500
s1.shows_makrs()
#Secure Data .......
class Student:
    def __init__(self,marks):
        self.__marks = marks

    def shows_marks(self):
        print('marks:',self.__marks)

s1 =Student(90)
s1.shows_marks()

s1.__marks = -500
s1.shows_marks()

#secure(Modify Safely).....
class Student:
    def __init__(self,marks):
        self.__marks = marks 
    
    def set__marks(self,marks):
        if marks >=0 and marks <=100:
            self.__marks = marks 
        else:
            print("Invalid marks")
        
    def get__marks(self):
        return self.__marks 
    
s1 =Student(90)
print(s1.__dict__)
s1.set__marks(100)
print("Modify marks :",s1.get__marks())

