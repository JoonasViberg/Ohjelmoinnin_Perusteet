########################################################
# Task A10_T5
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# Create a CLI program which can calculate factorial recursively. Collect factorial from the user input.

# Factorial definition (recursive):

# n! = n × (n − 1)!

# Factorial: 
# 1
# 1! = 1
# Factorial: 
# 1
# 1! = 1


# Implement the factorial function in recursive manner.
# This means that the factorial function should call itself as many times as required till the number is solved. Recursion causes the call stack to grow.

# The Code evaluator will check for recursiveFactorial function, which takes one positional argument PNum: int and returns the factorial result as an integer.
# It also checks for proper recursive behaviour.

# Note! This exercise is designed so you can practice how the recursion works.
# However, it is often recommended to avoid using recursive calls in programs.
# Recursive calls can lead to a stack overflow if the recursion depth exceeds the system’s maximum stack size.
# In Python, the interpreter raises a RecursionError in such cases.

# Example program runs:
# Program starting.
# Insert factorial: 1
# Factorial 1!
# 1 = 1
# Program ending.

# Example solution contains 32 lines of code.

import sys
from typing import NoReturn

def recursiveFactorial(PNum: int) -> int:
    # Base case: 0! and 1! both equal 1
    if PNum == 0 or PNum == 1:
        return 1
    
    # Recursive step: n * (n - 1)!
    return PNum * recursiveFactorial(PNum - 1)

def askNumber() -> int:
    while True:
        try:
            raw_input = input("Insert factorial: ")
            num = int(raw_input)
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
                continue
            return num
        except ValueError:
            print(f"Error: '{raw_input}' is not a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            sys.exit(1)

def main() -> None:
    print("Program starting.")
    
    try:
        n = askNumber()
        
        result = recursiveFactorial(n)
        
        print(f"Factorial {n}!")
        print(f"{n} = {result}")
        
    except RecursionError:
        print("Error: Recursion depth exceeded (Stack Overflow).")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
        
    print("Program ending.")

if __name__ == "__main__":
    main()