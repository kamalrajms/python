#list
fruits=["raj","tamil","kumar"]
print(fruits)
# access
print(fruits[2])
# modify
fruits[1]="santhosh"
print(fruits)
#adding items
fruits.append("cherry")
print(fruits)
fruits.insert(2,"mango")
print(fruits)
#remve items
fruits.pop(1)
print(fruits)

numbers=[10,3,5,2,6]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
tot=sum(numbers)
print(tot)

for i in numbers:
    print(i)

# tuple

color=("red","yellow","green")
print(color)
#access
print(color[2])

# set {}
number={1,2,3,4,4}
number.add(10)
number.remove(2)
print(number)

a={1,2,3,4}
b={3,4,5,6}

# in set we have mathematical operator

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(b ^ a)

# dictionary

student={
    "name":"john",
    "age":21,
    "course":"pyhon"
}
#access
print(student)
#modify
print(student["name"])
print(student["age"])
student["age"]=55
print(student)
#remove
student.pop("course")
print(student)
print(student.items())

for key,value in student.items():
    print(key, " : ",value)

#nested dictionary
student={
    1:{"name":"kumar","age":20},
    2:{"name":"raj","age":22}
}
print(student)
print(student[1])
print(student[1]["name"])
print(student[2]["age"])

#example for dictionary

marks = {
    "maths":90,
    "tamil":99
}
# print(marks.keys)
# print(marks.values)
tot=sum(marks.values())
avg=tot/len(marks)
print(avg)
