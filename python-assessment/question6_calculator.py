# Question 6: Function-Based Calculator
# Simple calculator program using separate functions for basic arithmetic operations.

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

print("=== Function-Based Calculator ===")
print("Available Operations: +, -, *, /")

# Take operation and numbers from user
choice = input("Enter operation (+, -, *, /): ").strip()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform selected operation
if choice == '+':
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '-':
    result = subtract(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '*':
    result = multiply(num1, num2)
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '/':
    result = divide(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation selected! Please choose +, -, *, or /.")
