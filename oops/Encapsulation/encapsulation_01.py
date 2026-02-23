class Student:
    def __init__(self):
        self.__marks = 90

s1 = Student()

print(s1.__marks) # Here it will gives error because in encapsulation , 
                # python actually converts it into _student__marks so when we run this it will the actual marks 
print(s1._Student__marks)
print(s1.__dict__)