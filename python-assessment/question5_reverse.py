def reverse_string():
    print("=== String Reversal ===")
    text = input("Enter a string: ")
    
    reversed_text = text[::-1]
    
    print(f"Reversed string: {reversed_text}")

if __name__ == "__main__":
    reverse_string()
