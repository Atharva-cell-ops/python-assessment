def check_even_odd():
    print("=== Even or Odd Checker ===")
    try:
        number = int(input("Enter an integer: "))
        
        if number % 2 == 0:
            print(f"{number} is an Even number.")
        else:
            print(f"{number} is an Odd number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    check_even_odd()
