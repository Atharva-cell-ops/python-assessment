# Question 3: Sum of Numbers from 1 to N
# Program to calculate the sum of all natural numbers from 1 to N.

def calculate_sum():
    print("=== Sum of Numbers from 1 to N ===")
    try:
        # Prompt user for a positive integer N
        n = int(input("Enter a positive integer (N): "))
        
        # Validate that the integer is positive
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return

        # Initialize total sum accumulator
        total_sum = 0
        
        # Use a for loop to iterate from 1 up to N (inclusive)
        for i in range(1, n + 1):
            total_sum += i
        
        # Display the result
        print(f"The sum of numbers from 1 to {n} is: {total_sum}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    calculate_sum()
