########################################################
# Task A10_T2
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# Create a program that can analyse integers in a text file.
# Filter empty rows and strip the newline characters so that each row can be converted into an integer datatype.

# Analysis:

# Calculate the sum of the numbers
# Calculate the product of the numbers
# Consider implementing the following aspects in the code:

# import sys # for possible exit on errors

# def readValues(PFilename: str, PValues: list[int]) -> None:
#     # ...
#     return None

# def sumOfValues(PValues: list[int]) -> int:
#     # ...
#     return Sum

# def productOfValues(PValues: list[int]) -> int:
#     # ...
#     return Product

# def main() -> None:
#     # 1. Initialize
#     Values: list[int] = []
#     # 2. Operate
#     print("Program starting.")
#     # 2.1 ask filename
#     # 2.2 read values
#     # 2.3 calculate sum of values
#     # 2.4 calculate product of values
#     # 2.5 display results
#     # 3. Cleanup
#     Values.clear()
#     print("Program ending.")
#     return None
# Display the results for the user in the same format as is in the program run below.

# Example program run:
# Program starting.
# Insert filename: A10_D10.txt
# # --- Sum of numbers --- #
# 3990
# # --- Sum of numbers --- #
# # --- Product of numbers --- #
# 3409038636128947261440000
# # --- Product of numbers --- #
# Program ending.

# Program will be tested with the provided data files: “A10_D10.txt”, “A10_D100.txt” and “A10_D1000.txt”.
# The end results may be quite long.

# Example solution contains 71 lines of code.

import sys
from typing import List

def readValues(PFilename: str, PValues: List[int]) -> None:
    try:
        with open(PFilename, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        value = int(line)
                        PValues.append(value)
                    except ValueError:
                        print(f"Error: Could not convert '{line}' to an integer. Skipping.")
                        
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
        
    return None

def sumOfValues(PValues: List[int]) -> int:
    Sum = 0
    for value in PValues:
        Sum += value
    return Sum

def productOfValues(PValues: List[int]) -> int:
    # Initialize product to 1, as multiplying by 0 results in 0
    Product = 1
    if not PValues:
        return 0
        
    for value in PValues:
        Product *= value
    return Product

def main() -> None:
    Values: List[int] = []
    print("Program starting.")
    
    # 2.1 ask filename
    filename = input("Insert filename: ")
    
    # 2.2 read values
    readValues(filename, Values)
    
    if not Values:
        print("No valid integers were loaded for analysis.")
        print("Program ending.")
        sys.exit(0)

    # 2.3 calculate sum of values
    total_sum = sumOfValues(Values)
    
    # 2.4 calculate product of values
    total_product = productOfValues(Values)
    
    # 2.5 display results
    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")
    
    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()