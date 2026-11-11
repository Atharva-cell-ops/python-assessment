def calculate_sum():
    print("=== Sum of Numbers from 1 to N ===")
    try:
        n = int(input("Enter a positive integer (N): "))
        
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        total_sum = 0
        
        for i in range(1, n + 1):
            total_sum += i
        
        print(f"The sum of numbers from 1 to {n} is: {total_sum}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    calculate_sum()
