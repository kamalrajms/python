class Animal:
    def sound(self):
        print("animals caan make sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meow")
for i in [Dog(),Cat()]:
    i.sound()

