# Question 5: Reverse a String
# Program to accept a string from the user and print its reverse.

print("=== String Reversal ===")

# Accept input string from the user
text = input("Enter a string: ")

# Reverse string using Python slicing syntax [start:stop:step]
# A step of -1 traverses the string backwards
reversed_text = text[::-1]

# Display the reversed string
print(f"Reversed string: {reversed_text}")
