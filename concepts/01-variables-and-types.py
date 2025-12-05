# Learning: Variables and Data Types
# Date: December 5, 2025
# Topic: Understanding Python variables, integers, floats, strings, and booleans

# 1. Variables - containers for storing data
name = "jonvsgithub"  # String variable
age = 25  # Integer variable
height = 5.9  # Float variable
is_learning = True  # Boolean variable

print(f"Name: {name}, Age: {age}, Height: {height}m, Learning: {is_learning}")

# 2. Different data types
integer_value = 42
float_value = 3.14
string_value = "Python is awesome!"
boolean_value = False

print(f"Int: {type(integer_value)}, Float: {type(float_value)}, String: {type(string_value)}")

# 3. Type conversion
str_number = "100"
converted_int = int(str_number)
print(f"String '100' converted to int: {converted_int}")

# 4. Variable naming conventions
myVariable = "camelCase"  # Not recommended in Python
my_variable = "snake_case"  # Recommended in Python
MyClass = "PascalCase"  # Used for class names

# Key Learning Points:
# - Variables don't need type declaration
# - Python uses dynamic typing
# - Follow snake_case naming convention
# - Use meaningful variable names
