# Question 2: Largest of Three Numbers
# Program to accept three numbers from the user and find the largest among them.

print("=== Largest of Three Numbers ===")

# Prompt user for three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Compare numbers using conditional statements (if-elif-else)
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the largest number
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
