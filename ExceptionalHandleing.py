try:
    num1=int(input("enter a number :"))
    num2=int(input("enter a another number :"))
    print(num1/num2)
except ZeroDivisionError:
    print("we can't divide it")

try:
    x=int(input("enter a number 1:"))
    y=int(input("enter a number 2:"))
    print("result  :", x/y)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("we can't divide it")
except Exception as e:
    print("Someting went wrong")

age=int(input("enter a ypur age :"))

if age<18:
    raise ValueError("you must be at least 18 years old")
else:
    print("Access granted")

