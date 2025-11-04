# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

# for i in range(10):
#     print("hello", i)

# for i in range(1,6):
#     print(i)

# for a in "python":
#     print(a)

# fruits=["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)
#     for i in fruit:
#         print(i)

# for i in range(2,11,5):
#     print(i)

# i=0
# while i<=5:
#     print(i)
#     i=i+1

# count=5
# while count>=0:
#     print("countdown",count)
#     count-=1
# print("blast off")
    
# break

# for i in range(1,7):
#     if i==4:
#         break
#     print(i)

# continue
for i in range(1,8):
    if i==3:
        continue
    print(i)


# else block with loop

for i in range(5):
    if i==4:
        break
    print(i)
else:
    print("loop comnpleted")

# nested for

for i in range(1,6):
    for j in range(1,6):
        print(i*j,end="\t")
    print()