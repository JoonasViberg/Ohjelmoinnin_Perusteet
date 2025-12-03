########################################################
# Task A10_T6
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# Create a menu-driven program which is able to measure nano seconds spent on sorting. In this exercise, use datasets A10_D10.txt, A10_D100.txt and A10_1000.txt.

# Implement and/or use three sorting algorithm:
# Built-in sorted
# Bubble sort
# Quick sort
# Build menu-driven program with 4 options
# 1 - Read dataset values
# 2 - Measure speeds
# 3 - Save results
# 0 - Exit
# Measure the sorting time on ascending order using the “time.perf_counter_ns()” function. Sorting time can be calculated by subtracting starting time from the stopping time.

# Functions can also be passed as an argument to other functions. Just omit the parentheses () when doing so. The datatype is Callable which can be imported from the typing library.

# Also copy the original dataset using for example copy.deepcopy function so that the next sorting algorithm doesn’t receive already sorted array. Import the copy module first.

# See code examples below:

# import copy
# import time
# from typing import Callable

# def readValues(PValues: list[int|float]) -> None:
#     # clear values list to ensure no duplicate data (reading twice)
#     # open filehandle
#     # read line-by-line
#     #   # parse value(int) from line(str + '\n')
#     #   # append value into the values list
#     # close filehandle
#     return None

# def quickSort(PNums: list[int]) -> list[int]:
#     # https://en.wikipedia.org/wiki/Bubble_sort
#     return PNums

# def bubbleSort(PNums: list[int]) -> list[int]:
#     # https://en.wikipedia.org/wiki/Quicksort
#     return PNums

# def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
#     StartTime = time.perf_counter_ns()
#     PSortingAlgorithm(PArr) # param is function
#     EndTime = time.perf_counter_ns()
#     ElapsedTime = EndTime - StartTime
#     return ElapsedTime

# def main() -> None:
#     # 1. Initialize
#     Values: list[int] = []
#     Results: list[str] = []
#     # 2. Operate
#     print("Program starting.")
#     readValues(Values)
#     # ...
#         # pass algorithm into the measureSortingTime function # import copy
#         BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
#         BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
#         # check if 
#     # 3. Cleanup
#     Values.clear()
#     Results.clear()
#     print("Program ending.")
#     return None
# Example program run:

# Note! the speed results may vary.
# Measuring speeds using “A10_D100.txt” or “A10_D1000.txt”, the built-in sorted should be the quickest, followed by quick sort and slowest sorting algorithm should be bubble sort..

# Program starting.
# Options:
# 1 - Read dataset values
# 2 - Measure speeds
# 3 - Save results
# 0 - Exit
# Your choice: 1
# Insert dataset filename: A10_D10.txt

# Options:
# 1 - Read dataset values
# 2 - Measure speeds
# 3 - Save results
# 0 - Exit
# Your choice: 2
# Measured speeds for dataset 'A10_D10.txt':
#  - Built-in sorted 16083 ns
#  - Buble sort 53875 ns
#  - Quick sort 49458 ns

# Options:
# 1 - Read dataset values
# 2 - Measure speeds
# 3 - Save results
# 0 - Exit
# Your choice: 3
# Insert results filename: A10_D10_Results.txt

# Options:
# 1 - Read dataset values
# 2 - Measure speeds
# 3 - Save results
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

# Saved results in files:

# A10_D10_Results.txt
# A10_D100_Results.txt
# A10_D1000_Results.txt

# Measured speeds for dataset 'A10_D10.txt':
#  - Built-in sorted 16083 ns
#  - Buble sort 53875 ns
#  - Quick sort 49458 ns

# Example solution contains 152 lines of code.

import sys
import copy
import time
from typing import List, Callable, Tuple, Any

# --- Sorting Algorithms ---

def bubbleSort(PValues: List[int]) -> List[int]:
    """Sorts a list in ascending order using Bubble Sort (O(n^2)). Returns a new list."""
    # Note: Bubble Sort is typically implemented in-place, but to match the signature 
    # of the built-in sorted(), we return a new sorted list. The measure function will handle the copying.
    n = len(PValues)
    arr = PValues[:] # Work on a mutable copy
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quickSort(PValues: List[int]) -> List[int]:
    """Sorts a list in ascending order using Quick Sort (O(n log n)). Returns a new list."""
    # Standard Quick Sort implementation (recursive, returning a new list)
    if len(PValues) <= 1:
        return PValues
    
    pivot = PValues[len(PValues) // 2]
    left = [x for x in PValues if x < pivot]
    middle = [x for x in PValues if x == pivot]
    right = [x for x in PValues if x > pivot]
    
    return quickSort(left) + middle + quickSort(right)

def builtInSorted(PValues: List[int]) -> List[int]:
    """Wrapper for Python's built-in sorted function."""
    return sorted(PValues)

# --- File I/O and Helpers ---

def readValues(PValues: List[int]) -> str:
    """Prompts for filename, reads integers, and populates PValues list."""
    PValues.clear()
    filename = input("Insert dataset filename: ")
    
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        PValues.append(int(line))
                    except ValueError:
                        print(f"Warning: Non-integer value '{line}' skipped.")
        return filename
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def askChoice() -> int:
    """Prompts the user for a menu choice."""
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 <= choice <= 3:
                return choice
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            sys.exit(0)

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def measureSortingTime(PSortingAlgorithm: Callable[[List[int]], List[int]], PArr: List[int]) -> int:
    """Measures the time taken (in ns) by the sorting algorithm."""
    # Deep copy the array to ensure the algorithm receives the original, unsorted data
    arr_copy = copy.deepcopy(PArr)
    
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(arr_copy)
    EndTime = time.perf_counter_ns()
    
    return EndTime - StartTime

# --- Main Logic ---

def main() -> None:
    Values: List[int] = []
    Results: List[str] = []
    current_filename = ""
    
    print("Program starting.")
    
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            current_filename = readValues(Values)
            if current_filename and Values:
                 print(f"Dataset '{current_filename}' loaded with {len(Values)} values.")
            
        elif choice == 2:
            if not Values:
                print("Error: Load dataset values (Option 1) first.")
                continue
                
            print(f"Measured speeds for dataset '{current_filename}':")
            
            # Note: We pass the function name (Callable) and the data.
            # The measureSortingTime function handles deep copying.
            
            # Run Built-in Sorted
            BuiltinSortedTimeNs = measureSortingTime(builtInSorted, Values)
            print(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
            
            # Run Bubble Sort
            BubbleSortTimeNs = measureSortingTime(bubbleSort, Values)
            print(f" - Buble sort {BubbleSortTimeNs} ns")
            
            # Run Quick Sort
            QuickSortTimeNs = measureSortingTime(quickSort, Values)
            print(f" - Quick sort {QuickSortTimeNs} ns")
            
            # Store results for Option 3
            Results.clear()
            Results.append(f"Measured speeds for dataset '{current_filename}':")
            Results.append(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
            Results.append(f" - Buble sort {BubbleSortTimeNs} ns")
            Results.append(f" - Quick sort {QuickSortTimeNs} ns")

        elif choice == 3:
            if not Results:
                print("Error: Measure speeds (Option 2) first.")
                continue
                
            filename = input("Insert results filename: ")
            print(f"Saving file to \"{filename}\"")
            
            try:
                with open(filename, 'w', encoding='UTF-8') as f:
                    f.write('\n'.join(Results) + '\n')
                print("Vector saved successfully!")
            except Exception as e:
                print(f"Error saving file: {e}")

        elif choice == 0:
            print("Exiting program.")
            break
            
    # 3. Cleanup
    Values.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()