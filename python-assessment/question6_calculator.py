def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def calculator():
    print("=== Function-Based Calculator ===")
    print("Available Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        choice = input("Enter operation choice (+, -, *, / or 1, 2, 3, 4): ").strip()
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice in ('1', '+', 'add', 'Add'):
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice in ('2', '-', 'subtract', 'Subtract'):
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice in ('3', '*', 'multiply', 'Multiply'):
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice in ('4', '/', 'divide', 'Divide'):
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid operation selected! Please choose +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()
