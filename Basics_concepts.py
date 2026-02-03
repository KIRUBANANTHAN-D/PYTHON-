#1️⃣ Print & Comments
print("Hello World") 
#-------------------------------------------------------------------

#2️⃣ Variables & Data Types
name = "Kiruba"      # string
age = 22             # integer
waight = 55.5        # float
is_student = True    # boolean
skills = ["python","html","css","javascript","sql"]    # list
projects = ("bike-zone","cakeshop website")            # tuple
MY_data = {Name:"kiruba",age:20,location="chennai"}    # Dictionary
#-------------------------------------------------------------------
#3️⃣ Input from User
name = input("Enter your name: ")
print("Hello", name)
#-------------------------------------------------------------------
#4️⃣ Type Casting
age = int(input("Enter age: "))
price = float("10.5")
#-------------------------------------------------------------------
#5️⃣ Operators
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # modulus
#-------------------------------------------------------------------
#6️⃣ Conditions (if / else)
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
#-------------------------------------------------------------------
#7️⃣ Loops
for loop
for i in range(5):
    print(i)

while loop
i = 1
while i <= 5:
    print(i)
    i += 1
#-------------------------------------------------------------------
#8️⃣ Strings
text = "Python"

print(text.upper())
print(text.lower())
print(len(text))
print(text[0])
#-------------------------------------------------------------------
#9️⃣ Lists
nums = [1, 2, 3, 4]

nums.append(5)
print(nums)
#-------------------------------------------------------------------
#🔟 Tuples
data = (10, 20, 30)
print(data[0])
#-------------------------------------------------------------------
#1️⃣1️⃣ Sets
s = {1, 2, 3, 3}
print(s)   # duplicates removed
#-------------------------------------------------------------------
#1️⃣2️⃣ Dictionary
student = {
    "name": "Kiruba",
    "age": 22
}

print(student["name"])
#-------------------------------------------------------------------
#1️⃣3️⃣ Functions
def add(a, b):
    return a + b

print(add(2, 3))
#-------------------------------------------------------------------
#1️⃣4️⃣ Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
#-------------------------------------------------------------------
#1️⃣5️⃣ File Handling
f = open("data.txt", "w")
f.write("Hello Python")
f.close()
#-------------------------------------------------------------------
#1️⃣6️⃣ Exception Handling
try:
    x = int("abc")
except:
    print("Error occurred")
#-------------------------------------------------------------------
#1️⃣7️⃣ Modules
import math
print(math.sqrt(16))
#-------------------------------------------------------------------
#1️⃣8️⃣ OOP (Basic)
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s = Student("Kiruba")
s.show()
#-------------------------------------------------------------------
