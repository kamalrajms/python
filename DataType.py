# numerb type

x=1
y=2.8
z=1j
print(x)
print(y)
print(z)

x=int(1)
y=int(2.8)
z=int("3")
print(x)
print(y)
print(z)

x=float(1)
y=float(2.8)
z=float("3")
print(x)
print(y)
print(z)

# string type

# string

a="hello"
print(a)

# slicing string

b="hello world"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

# string Modifying

a="Hello, World    "
print(a.upper())
print(a.lower())
print(a.strip())

#string concordination

a="hello"
b="world kumar"
c=a+" "+b
print(c)

#string format

c=34

txt=f"my age is {c}"
print(txt)

## boolean type

print(10>5)
print(10==9)
print(10>9)
print(10>=9)
print(10<9)
print(10<=9)

## none type

a=None
print(a)

# operators
# arithmetic opreator

a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# assignement

a=10
b=5
a+=b
# a=a+b
# a=a+3
print(a)

# Comparison operatior

x=5
y=6
print(x==y)
print(x>=y)
print(x<y)

#logical operatior

x=55 
y=56

print((x>y)&(x<y))

#membership operator

x=["apple","banana"]
print("banana" in x)
print("mango" not in x)

# bitwise operators

x=8    
y=3
print(x^y)

# list

a=["apple","mango","banana"]
print(a)
print(a[0])
print(a[-2])
a[2]="orange"
print(a[2:3])
a.insert(2,"grapes")
a.remove("apple")
b=[1,2,3,4,5]
b.pop()
b.extend([8,9,0])
b.sort()
print(b)
