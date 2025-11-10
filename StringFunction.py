name="hari"
print(name)
name='hari'
print(name)
name=""" this
 is 
 a  program.
"""
print(name)

word="pyhon"
print(word[0])
print(word[3])

# string slicing

text="python programming"
print(text[0:4])
print(text[7:])
print(text[:6])
# step slicing
word="Hello"
print(word[::2])
print(word[::-1])
print(word[::])
# string concatenation
first="Helllo"
second="World"
print(first + " "+ second)
# srting function
word="python Programming"
print(len(word))
print(word.upper())
print(word.lower())
print(word.title())
word="    pyhon is very easy  "
print(word.strip())
text="i like apples"
print(text.replace("apples","mangos"))
new=text.split()
print(new)
worsd=["pyhton","is" ,"fun"]
text=" ".join(worsd)
print(text)
text="banana"
print(text.count("a"))
text1="python Programming"
print(text1.find("Pro"))
text="pyhton"
print(text.startswith("py"))
print(text.endswith("on"))
# string Comparison
a="apple"
b="cat"
print(a==b)
print(a<b)
# checking char in str
text="learning python"
print("python" in text)
print("java" not in text)







