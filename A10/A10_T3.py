########################################################
# Task A10_T3
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# Bubble sort is a well-known sorting algorithm that is renowned for its simplicity in understanding and implementation.
# The bubble sort algorithm organizes a list of items in either ASCending or DESCending order by repeatedly iterating through the list.
# During each iteration, it compares adjacent elements and swaps them if they are in the wrong order.
# After the first iteration, the largest (or smallest, depending on the sorting order) element will be correctly placed at the end of the list.
# The process then repeats for the remaining unsorted elements.

# Remaining = Items(n) − Iteration − 1

# Here, n refers to the total number of items in the list. 
# he Big-O notation for bubble sort is O(n2), indicating that its runtime increases quadratically with the number of items.
# This is because the algorithm involves two nested loops.
# An outer loop for the iterations and an inner loop for comparisons and swaps.

# The Iteration in bubble sort corresponds to the current pass (or cycle) of the outer loop.
# It tracks how many times the list has been processed.
# The very first iteration is numbered as 0, and the last iteration occurs just before the list length.

# LastIteration = Length − 1

# The “magic number” -1 in the remaining formula is often used in implementations of bubble sort to prevent out-of-bound errors.
# This is because the algorithm compares each element with its next neighbor in the list.
# By iterating only up to n − Iteration − 1, it ensures that the last comparison in each pass stays within the valid range of the list.
# Additionally, this optimization reduces one unnecessary comparison on each outer cycle, improving the algorithm’s efficiency.

# On other notes, bubble sort may be easy to implement, but it is not very efficient for large inputs when compared to some other sorting algorithms.

# Visit wikipedia: Bubble sort and see the pseudocode implementation. Use it or some other source as a guide to build the sorting algorithm.
# Once done, ensure that the function is pure and has the interface as defined below(naming, parameters and return values).
# The bot will extract the function based on the A10_T3.py implementation.
# If you have used A10_TLib.py to store the algorithm, the bot should be able to extract it from there too.

# After the sorting algorithm is extracted successfully, it will test if the sorting algorithm works.
# Then it compares the extracted bubble sort algorithm into another algorithm to determine if the speed aligns with the expectations (BigO notation).

# Interface to implement. Note parameter PAsc is set by default to True.
# This means that the algorithm should sort everything in ascending order by default if only one argument is passed.

# def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
#     # Sort PValues by implementing bubble sort algorithm.
#     # Handle PValues list like it is a pointer to memory
#     # Sort the list inplace e.g., PValues[CurrentIndex] = PValues[NextIndex]
#     # Don't overwrite PValues identifier.
#     # Tester expects that the PValues list is modified.
#     # It doesn't catch a return value.
#     return None
# For the main program, prompt filename if there are no CLI arguments to the program. In case the len(sys.argv) is 2, then take the second argument (sys.argv[1]) and use it as a filename.

# Commands:

# # Tab 1 - Insert dataset name 'A10_D10.txt' manually
# python A10_T3.py 
# # Tab 2 - CLI Argument (sys.argv[1])
# python A10_T3.py A10_D10.txt
# # Tab 3 - CLI Argument (sys.argv[1])
# python A10_T3.py A10_D100.txt
# Example program runs:
# Program starting.
# Insert filename: A10_D10.txt
# Raw 'A10_D10.txt' -> 1000, 221, 392, 621, 47, 448, 163, 120, 197, 781
# Ascending 'A10_D10.txt' -> 47, 120, 163, 197, 221, 392, 448, 621, 781, 1000
# Descending 'A10_D10.txt' -> 1000, 781, 621, 448, 392, 221, 197, 163, 120, 47

# Example bubble sort solution contains ~30 lines of code.

import sys
from typing import List

# --- START: Content from A10_Tlib.py ---
def bubbleSort(PValues: List[int], PAsc: bool = True) -> None:
    n = len(PValues)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            
            should_swap = False
            
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    should_swap = True
            else:
                if PValues[j] < PValues[j + 1]:
                    should_swap = True
                    
            if should_swap:
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                
    return None
# --- END: Content from A10_Tlib.py ---


def readFileContent(PFilename: str) -> List[int]:
    data = []
    try:
        with open(PFilename, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        data.append(int(line))
                    except ValueError:
                        print(f"Error: Non-integer value '{line}' found in file. Skipping.")
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    return data

def displayData(PName: str, PFilename: str, PData: List[int]) -> None:
    print(f"{PName} '{PFilename}' -> {', '.join(map(str, PData))}")

def main() -> None:
    print("Program starting.")
    
    filename = ""
    
    # Handle CLI Arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        # Prompt for filename if no CLI argument is provided
        filename = input("Insert filename: ")
        
    # Read Values
    raw_data = readFileContent(filename)
    
    if not raw_data:
        print("No data loaded. Program ending.")
        sys.exit(0)
        
    # Create copies for in-place sorting
    data_asc = raw_data[:]
    data_desc = raw_data[:]
    
    # 1. Display Raw Data
    displayData("Raw", filename, raw_data)
    
    # 2. Ascending Sort and Display
    bubbleSort(data_asc)
    displayData("Ascending", filename, data_asc)
    
    # 3. Descending Sort and Display
    bubbleSort(data_desc, PAsc=False)
    displayData("Descending", filename, data_desc)
    
    print("Program ending.")

if __name__ == "__main__":
    main()