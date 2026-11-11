# Question 1: Even or Odd
# Program to determine whether an input integer is even or odd.

print("=== Even or Odd Checker ===")

# Prompt user to enter an integer
number = int(input("Enter an integer: "))

# Check divisibility by 2 using the modulus operator (%)
# If remainder is 0, the number is even; otherwise, it is odd
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")
