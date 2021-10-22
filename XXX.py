# int a = 6;
# float b = 6.9;
# int float str bool

print("gshagd")
print(5)
print(True)

print("Hi" + "Hello")
print("Hi","Hello")
print("Hi "*5)

print('Hello')
print("Hello")
print("""I 
Am Multi
Line String""")
d = 5
print("%d I am Integetr"%(d)) # d, I am 
name = 'Akash'
sName = 'Bajpai'

print("My Name is", name, "My Sir Name is", sName)
print(f"My Name is {name} and My Surname is {sName}")
print("My Name is {} and My Sirname is {}".format(name, sName))

# Operator
# * , **
print(5*3)
print(5**3)

print(5/3)
print(5//3)
print(5%3)

# False -> 0
# True -> 1
print(True + False)
print(True and False)
print(True or False)
print(not False)
a = "Hello"
print(type(a))

print(23/7)
print(round(23/7, 5))

# In Python We can only take string as input
# a = int(input("Enter The Number >>>>"))
# print(type(a))

# Strings

b = "Adarsh"
c = str(5)

d = "Akash Bajpai"
print(d[1])
# "Hello"
# 0 1 2 3 4
# -5 -4 -3 -2 -1
print(d[-3])

# "Hello" -> "ell"
# String Slicing -> varName[startIndex(inclusive),default Value = 0 : endIndex(exclusive), value = lenOfString, stepValue]

print(d[1:5])
print(d[-5:])

print(d[::2])

print(d.index('k'))

print("Hello".count('l'))

num = int(input("Enter The Number >>> "))
if num > 10:
    print("Number is greater than 10")
elif num >= 5 and num <= 10:
    print("I am b/w 5 and 10")
else:
    print("I am a Number")

# if num > 10:
#     if num2 < 5:
#         print("Bye")
#     else:
#         print("heloo")

# while for while elese for else
# i = 0
# while i<5:
#     print(i)
#     i += 1
# else:
#     print("Given Condition become false with value of i =", i)

# range(0,5) -> rangeObject -> [0,1,2,3,4]
# range(0,5,2) -> [0,2,4]

d = "Aakash"
for i in range(0,5,2):
    print(i, end='')

for i in range(5):
    for j in range(3):
        print("*")

# File Handling

fileName = open("H.txt", "r") # If d
# print(fileName)
fileData = fileName.read()
print(fileData)
fileName.close()

fileName = open("H.txt", "w")
fileName.write("Rana is \n OP")
fileName.close()

fileName = open("H.txt", "a")
fileName.write("I am New \n Addded Lines")
fileName.close()

fileName = open("H.txt", "r")
print(fileName.readline(3))
fileName.close()

fileName = open("H.txt", "r")
filelines = fileName.readlines()
print(filelines)
fileName.close()

# List
for aksh in filelines:
    print(aksh.strip())

# List
a = [1, "Adarsh", 3.45, False, [1,3.5]]
# Accessing Elements is smae as styring
print(a)
print(a[1])
print(a[-1][1])

# Slicing is done same as string
print(a[2::2])

a = [1,2,3,4,5]
a.append("Hello")
a.append(6)
print(a)

a.insert(100, "I am at 4th Index")
print(a)

a.pop(2)
print(a)

# a.remove("Hello2")
# print(a)

a = [1,2,1,3,1,1,1]
print(a.count(1))

a.remove(1)
print(a)

a = [1,2,3]
print(1 in a)

for each in a:
    print(each, end=' * ')

for i in range(0, len(a)):
    print(a[i], end= ' * ')

# Dictionary

student = ["Akash", "Bajpai", "B.tech", 5]
student = {"name": "akash", "surname": "Bajpai", "degree": "B.tech", "age": 5}
print(student["name"])
print(student["surname"])
print(student["age"])

print(student.get("name2"))

student["Father"] = "God"
print(student)

print(list(student.keys()))
print(student.values())
print(student.items())

a, b = [4, 5]

for (key, value) in student.items():
    print(key, "->", value)

a = [1, 1, 2, 3, 4, 4, 4, 4]
d = dict()
for each in a:
    d[each] = a.count(each)
for (key, value) in d.items():
    print(key, "->", value)


d = {"Hey": "Hello"}
d["Bye"] = "Hello"
print(d)

d.update({"Key1": 5, "Key2": 6})
print(d)

# Tuple
a = [1,2,3]
a[1] = "Hello"
print(a)

tup = (1,2,3,5)
# tup[1] = 8
print(tup)
tup = 'Adarsh'
# Immutable -> string, int, float, tuple
# Mutable 
# d = 'Hi'
# d[1] = 'O'

a = (5,) # Singleton
print(a, type(a))

# del a
# print(a)

a = (1,2,3)
a = list(a)
a.append(4)
a = tuple(a)
print(a)

# Functions 
def NameOfFunction(a, b=0):
    print(a, b)
    return a+b
# print(NameOfFunction(5,6))
# print(NameOfFunction(b=15, a=6))
NameOfFunction(15,21)

a = NameOfFunction(5,21)
print(a)

# Lambda expressions
mul = lambda a,b: a*b
# def mul(a,b):
#     return a*b

print(mul(2,5))

def boy(c,d):
    return c*d

def ares():
    print("A Called")
    return boy(5,4)

print(ares())

