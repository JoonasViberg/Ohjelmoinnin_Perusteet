# Create a menu-driven program which is able to read timestamps and count timestamps based on “year”, “month” or “weekday”.
# Use both provided datasets: “A8_T1D1.txt” and “A8_T1D2.txt”.

# Datasets
# A8_T4_D1.txt
# A8_T4_D2.txt
# For handling the timestamps use the “datetime” library and look for the datetime library documentation aspects:

# strptime and format directives %Y, %m, %d, %H and %M
# year
# month
# day
# Recommended things to implement into the library file:

# MONTHS: list[str] containing month names
# WEEKDAYS: list[str] containing weekday names
# def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
# def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
# def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
# def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
# Weekdays and months can be defined as constant variables in the program top-level. e.g.,

# MONTHS = (
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# )

# WEEKDAYS = (
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday"
# )

# Example program runs:

# Program starting.
# Insert filename: A8_T4_D1.txt
# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 1
# Insert year: 2000
# Amount of timestamps during year '2000' is 3

# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 2
# Insert month: April
# Amount of timestamps during month 'April' is 2

# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 3
# Insert weekday: Monday
# Amount of timestamps during weekday 'Monday' is 3

# Options:
# 1 - Calculate amount of timestamps during year
# 2 - Calculate amount of timestamps during month
# 3 - Calculate amount of timestamps during weekday
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

import timestamp_library
from datetime import datetime
from typing import List

# Import all specific functions and constants for cleaner access
from timestamp_library import (
    readTimestamps, calculateYears, calculateMonths, 
    calculateWeekdays, WEEKDAYS, MONTHS
)

def showOptions() -> None:
    """Displays the menu options to the user."""
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    """Prompts the user for a menu choice."""
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main() -> None:
    print("Program starting.")
    
    # 1. Load Data
    timestamps: List[datetime] = []
    
    filename = input("Insert filename: ")
    
    try:
        # Use the imported function to read and populate the list
        readTimestamps(filename, timestamps)
    except FileNotFoundError:
        # Error message is printed inside readTimestamps
        print("Program ending.")
        return
        
    if not timestamps:
        print("No valid timestamps were loaded. Program ending.")
        return

    # 2. Menu Loop
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break

        if choice == 1:
            # Calculate amount of timestamps during year
            try:
                year = int(input("Insert year: "))
                count = calculateYears(year, timestamps)
                print(f"Amount of timestamps during year '{year}' is {count}")
            except ValueError:
                print("Invalid year input. Please enter a number.")
        
        elif choice == 2:
            # Calculate amount of timestamps during month
            month = input("Insert month: ").strip().capitalize()
            if month not in MONTHS:
                 print(f"Error: Invalid month name. Must be one of: {', '.join(MONTHS)}.")
                 continue

            count = calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}")
        
        elif choice == 3:
            # Calculate amount of timestamps during weekday
            weekday = input("Insert weekday: ").strip().capitalize()
            if weekday not in WEEKDAYS:
                print(f"Error: Invalid weekday name. Must be one of: {', '.join(WEEKDAYS)}.")
                continue

            count = calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}")

    print("Program ending.")

if __name__ == "__main__":
    main()