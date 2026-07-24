# Variables and Data Types
name = "Saloni"          # string
age = 21                 # integer
height = 5.4              # float
is_student = True         # boolean
print(name, age, height, is_student)

#Operators
a = 10
b = 3
print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a % b)   # remainder
print(a > b)   # comparison → True/False

#Loops
# for loop
for i in range(1, 6):
    print("Number:", i)

# while loop
count = 1
while count <= 5:
    print("Count is", count)
    count += 1

#Functions
def greet(name):
    print("Hello,", name, "! Welcome to Day 2.")

greet("Saloni")
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 7)
print("Sum:", result)   

#Simple Program
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

for n in range(1, 11):
    print(n, "is", check_even_odd(n))