# Exercise 1: Basic Python Practice
# Date: December 5, 2025
# Difficulty: Beginner

# Exercise 1.1: Create variables and print them
print("=== Exercise 1.1: Variables ===")
student_name = "jonvsgithub"
student_age = 25
gpa = 3.8

print(f"Student: {student_name}, Age: {student_age}, GPA: {gpa}")

# Exercise 1.2: Perform calculations
print("\n=== Exercise 1.2: Calculations ===")
num1 = 15
num2 = 4
print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")
print(f"Average: {(num1 + num2) / 2}")

# Exercise 1.3: String manipulation
print("\n=== Exercise 1.3: Strings ===")
first_name = "Jon"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Length: {len(full_name)}")

# Exercise 1.4: Boolean expressions
print("\n=== Exercise 1.4: Boolean Logic ===")
age = 25
is_adult = age >= 18
print(f"Is adult: {is_adult}")
print(f"Can vote: {is_adult and age >= 18}")

# Challenge: Create a simple calculator
print("\n=== Challenge: Simple Calculator ===")
def simple_calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

result = simple_calculator(20, 5, '+')
print(f"20 + 5 = {result}")
