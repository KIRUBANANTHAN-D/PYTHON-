#1️) Print & Comments
print("Hello World") 
#-------------------------------------------------------------------

#2️) Variables & Data Types
name = "Kiruba"      # string
age = 22             # integer
waight = 55.5        # float
is_student = True    # boolean
skills = ["python","html","css","javascript","sql"]    # list
projects = ("bike-zone","cakeshop website")            # tuple
MY_data = {Name:"kiruba",age:20,location="chennai"}    # Dictionary
#-------------------------------------------------------------------
#3️) Input from User
name = input("Enter your name: ")
print("Hello", name)
#-------------------------------------------------------------------
#4️) Type Casting
age = int(input("Enter age: "))
price = float("10.5")
#-------------------------------------------------------------------
#5️) Operators
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # modulus
#-------------------------------------------------------------------
#6️) Conditions (if / else)
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
#-------------------------------------------------------------------
#7️) Loops
for loop
for i in range(5):
    print(i)

while loop
i = 1
while i <= 5:
    print(i)
    i += 1
#-------------------------------------------------------------------
#8️) Strings
text = "Python"
print(text.upper())
print(text.lower())
print(len(text))
print(text[0])
#-------------------------------------------------------------------
#9️) Lists
nums = [1, 2, 3, 4]

nums.append(5)
print(nums)
#-------------------------------------------------------------------
#10) Tuples
data = (10, 20, 30)
print(data[0])
#-------------------------------------------------------------------
#1️1️)
Sets
s = {1, 2, 3, 3}
print(s)   # duplicates removed
#-------------------------------------------------------------------
#1️2️) Dictionary
student = {
    "name": "Kiruba",
    "age": 22
}

print(student["name"])
#-------------------------------------------------------------------
#1️3️) Functions
def add(a, b):
    return a + b

print(add(2, 3))
#-------------------------------------------------------------------
#1️4️) Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
#-------------------------------------------------------------------
#1️5️) File Handling
f = open("data.txt", "w")
f.write("Hello Python")
f.close()
#-------------------------------------------------------------------
#1️6️) Exception Handling
try:
    x = int("abc")
except:
    print("Error occurred")
#-------------------------------------------------------------------
#1️7️) Modules
import math
print(math.sqrt(16))
#-------------------------------------------------------------------
#1️8️) OOP (Basic)
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s = Student("Kiruba")
s.show()
#-------------------------------------------------------------------
