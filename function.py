# print("hello tamil")
# print("hello tamil")
# print("hello tamil")
# print("hello tamil")

def hello():
    print("hello tamil")

hello()
hello()

# function with parameter and argument

def greet(name):
    print("welcome",name,"!")

greet("kamal")
greet("tamil")
greet("kumar")

def add_number(a,b):
    print("sum",a+b)
add_number(5,3)
add_number(5,1)
add_number(5,5)

# function with return value

def multiply(a,b):
    return a * b
ret=multiply(5,3)
s=ret*3
print("result",s)

def calculate(a,b):
    sums=a+b
    diff=a-b
    return sums,diff
a,b=calculate(10,5)
# print("value", a)
print("sum", a)
print("diff", b)

#tyes of functional arguments
#positional arg

def student_info(name,age):
    print("name",name)
    print("age",age)

student_info("raj",11)
student_info(55,"siva")
# keyword arg

def info(city,pin):
    print("city",city)
    print("pin code",pin)

info("salem",69898)
info(69898,"namakkal")
info(pin=606554,city="chennai")
# default arg
def greet(name="unknown person"):
    print("hello",name)
greet("kamal")
greet()

#variable length arg

#*arg-- multiple positional arg

def print_info(*number):
    for i in number:
        print(i)
    total=sum(number)
    print("total",total)



print_info(1,2,3,4,5)
print_info(10,20,30)

#**kwargs--multiple keyword arg

def user(**details):
    print(details)
    for key,value in details.items():
        print(key,":",value)
    

user(name="kamal",city="salem")
 
# scope of variable

# local scope

def show():
    message="hello"
    print(message)
show()

#global scope
pop="hello global"
def display():
    print(pop)
display()
print(pop)

#locl vs global

x=5
def show():
    x=10
    print("inside function",x)
show()
print("outsid a function",x)

# modify global variable inside a function

c=10

def change():
    global c
    c=30
    print(c)
change()
print(c)
# nested function

def outer():
  
    def inner():
        print("inner function")
   
    inner()
    print("outer function")
outer()



