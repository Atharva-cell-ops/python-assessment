# Python Basics – Programming Assessment

This repository contains solutions to the **Python Fundamentals Programming Assessment**. Each problem is implemented in a separate Python script, adhering strictly to core Python fundamentals without relying on external libraries or advanced object-oriented features.

---

## 📁 Repository Structure

```text
python-assessment/
│
├── question1_even_odd.py      # Checks if an integer is even or odd
├── question2_largest.py       # Finds the largest among three numbers
├── question3_sum.py           # Calculates the sum of natural numbers from 1 to N
├── question4_vowels.py        # Counts vowels in a string
├── question5_reverse.py       # Reverses a given string
└── question6_calculator.py    # Function-based arithmetic calculator
```

---

## 📋 Problems & Descriptions

### 1. Even or Odd (`question1_even_odd.py`)
- **Description**: Takes an integer as input and checks if it is divisible by 2 using the modulus operator (`%`).
- **Concepts**: User input, type casting (`int`), modulo operator, `if-else` conditionals.

### 2. Largest of Three Numbers (`question2_largest.py`)
- **Description**: Accepts three numbers and compares them using logical operators (`and`) to find the largest value.
- **Concepts**: Multiple user inputs, floating-point numbers, relational and logical operators, `if-elif-else` conditionals.

### 3. Sum of Numbers from 1 to N (`question3_sum.py`)
- **Description**: Takes a positive integer `N` and calculates the cumulative sum from `1` to `N` using a loop.
- **Concepts**: Input validation, accumulator variables, `for` loop, `range()` function.

### 4. Count Vowels in a String (`question4_vowels.py`)
- **Description**: Prompts the user for a string and counts all vowels (`a, e, i, o, u`, case-insensitive).
- **Concepts**: String traversal, membership operator (`in`), loop iteration, counter variable.

### 5. Reverse a String (`question5_reverse.py`)
- **Description**: Takes a string and produces its reverse using Python slicing (`[::-1]`).
- **Concepts**: String indexing and slicing.

### 6. Function-Based Calculator (`question6_calculator.py`)
- **Description**: Performs arithmetic operations using dedicated functions:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
  - `divide(a, b)` (handles division by zero)
- **Concepts**: Defining functions (`def`), return statements, function calls, basic error handling.

---

## 🚀 How to Run

Make sure you have Python 3 installed. Open a terminal / command prompt in this directory and execute any script:

```bash
# Question 1
python python-assessment/question1_even_odd.py

# Question 2
python python-assessment/question2_largest.py

# Question 3
python python-assessment/question3_sum.py

# Question 4
python python-assessment/question4_vowels.py

# Question 5
python python-assessment/question5_reverse.py

# Question 6
python python-assessment/question6_calculator.py
```
