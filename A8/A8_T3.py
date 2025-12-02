# Create a menu-driven program for analysing number files.
# Datasets
# A8_T3_D1.txt
# A8_T3_D2.txt
# Menu options:

# Read values
# Amount of values
# Calculate sum of values
# Calculate average of values
# The recommendation during the “readValues” operation is to skip the empty rows “\n” and convert the rows into floating point values.
# Values can be stored into a list[float] data structure.

# The amount of values can be calculated directly by using the “len”- function for the values list.
# For analysing (options 3 and 4), pass the list of values as an argument to some specific function.
# After calculating the sum or the average, round the results to one decimal precision. E.g. “1.234” => “1.2”

# Example program runs:
# Program starting.
# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 1
# Insert filename: A8_T3_D1.txt

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 2
# Amount of values 5

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 3
# Sum of values -115.5

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 4
# Average of values -23.1

# Options:
# 1 - Read values
# 2 - Amount of values
# 3 - Calculate sum of values
# 4 - Calculate average of values
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

import os

def readValuesFromFile(PFilename: str) -> list[float]:
    """Reads floating point values from a file, skipping empty lines."""
    values: list[float] = []
    if not os.path.isfile(PFilename):
        print(f"File '{PFilename}' does not exist.")
        return values

    with open(PFilename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    value = float(line)
                    values.append(value)
                except ValueError:
                    print(f"Invalid value '{line}' skipped.")
    return values
def calculateSum(PValues: list[float]) -> float:
    """Calculates the sum of a list of floating point values."""
    return round(sum(PValues), 1)
def calculateAverage(PValues: list[float]) -> float:
    """Calculates the average of a list of floating point values."""
    if len(PValues) == 0:
        return 0.0
    return round(sum(PValues) / len(PValues), 1)
def showOptions() -> None:
    """Displays the menu options to the user."""
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
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
def main() -> None:
    print("Program starting.")
    values: list[float] = []

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            filename = input("Insert filename: ")
            values = readValuesFromFile(filename)
        elif choice == 2:
            print(f"Amount of values {len(values)}")
        elif choice == 3:
            total_sum = calculateSum(values)
            print(f"Sum of values {total_sum}")
        elif choice == 4:
            average = calculateAverage(values)
            print(f"Average of values {average}")

    print("Program ending.")

if __name__ == "__main__":
    main()