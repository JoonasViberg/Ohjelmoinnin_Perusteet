# Create a menu-driven program which can perform basic arithmetic operations.
# All the math operations should be performed with floating datatype and without rounding.
# Separate the functionality into the appropriate files.

# Recommended subprogram names for the main file:

# def main() -> None:
# def showOptions() -> None:
# def askChoice() -> int:
# def askValue(PPrompt: str) -> float:
# Recommended subprogram names for the library file:

# def add(PAddend1: float, PAddend2: float) -> float:
# def subtract(PMinuend: float, PSubtrahend: float) -> float:
# def multiply(PMultiplicant: float, PMultiplier: float) -> float:
# def divide(PDividend: float, PDivisor: float) -> float:
# Example program runs:

# Program starting.
# Options:
# 1 - Add
# 2 - Subtract
# 3 - Multiply
# 4 - Divide
# 0 - Exit
# Your choice: 1
# Insert first addend value: 2
# Insert second addend value: 3
# 2.0 + 3.0 = 5.0

# Options:
# 1 - Add
# 2 - Subtract
# 3 - Multiply
# 4 - Divide
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

import math_library

def showOptions() -> None:
    """Displays the menu options to the user."""
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    """Prompts the user for a menu choice and handles input validation."""
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def askValue(PPrompt: str) -> float:
    """Prompts the user for a floating-point value and handles input validation."""
    while True:
        try:
            # Note: The input function is called using the provided prompt
            value = float(input(PPrompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main() -> None:
    print("Program starting.")
    
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        # Ask for two float values
        if choice == 1:
            val1 = askValue("Insert first addend value: ")
            val2 = askValue("Insert second addend value: ")
            result = math_library.add(val1, val2)
            print(f"{val1} + {val2} = {result}")
        
        elif choice == 2:
            val1 = askValue("Insert minuend value: ")
            val2 = askValue("Insert subtrahend value: ")
            result = math_library.subtract(val1, val2)
            print(f"{val1} - {val2} = {result}")
        
        elif choice == 3:
            val1 = askValue("Insert multiplicand value: ")
            val2 = askValue("Insert multiplier value: ")
            result = math_library.multiply(val1, val2)
            print(f"{val1} * {val2} = {result}")
        
        elif choice == 4:
            val1 = askValue("Insert dividend value: ")
            val2 = askValue("Insert divisor value: ")
            
            if val2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            
            result = math_library.divide(val1, val2)
            print(f"{val1} / {val2} = {result}")

    print("Program ending.")

if __name__ == "__main__":
    main()