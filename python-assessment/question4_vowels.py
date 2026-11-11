# Question 4: Count Vowels in a String
# Program to count the number of vowels (a, e, i, o, u) present in a given string.

print("=== Vowel Counter ===")

# Accept input string from user
text = input("Enter a string: ")

# Define the vowels (both lowercase and uppercase for case-insensitivity)
vowels = "aeiouAEIOU"
vowel_count = 0

# Iterate through each character in the string
for char in text:
    if char in vowels:
        vowel_count += 1

# Display the result
print(f"Total number of vowels in '{text}': {vowel_count}")
