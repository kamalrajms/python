# class & object
class car:
    def start(self):
        print("car Started")
    def stop(self):
        print("car Stoped")

car1=car()
car2=car()
car1.start()
car2.stop()

# constructor

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name},age:{self.age}")

s1=Student("Tamil",22)
s2=Student("hari",22)
s1.display()
s2.display()


# class variable and instance variable
class Student:
    shool="ABC school"   # class variable
    def __init__(self,name):
        self.name=name   #instance variable

x1=Student("Priya")
x2=Student("mani")

print(x1.name,x1.shool)
print(x2.name,x2.shool)

# types  of method in class

class Student:
    school="Xyz school"

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def show(self):     # instance method
        print(f" name:{self.name} scored : {self.mark}")

    @classmethod
    def change_school(cls,newName):
        cls.school=newName      #class method

    @staticmethod
    def greet():
        print("welcome to the school...")

Student.greet()
c1=Student("AHri",90)
c1.show()

Student.change_school("gergeg school")
print(Student.school)



        
        
        

