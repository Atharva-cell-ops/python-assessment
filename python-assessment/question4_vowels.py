def count_vowels():
    print("=== Vowel Counter ===")
    text = input("Enter a string: ")
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
            
    print(f"Total number of vowels in '{text}': {vowel_count}")

if __name__ == "__main__":
    count_vowels()
