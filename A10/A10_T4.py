########################################################
# Task A10_T4
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# Merge sort is a divine-and-conquer sorting algorithm that splits an array into smaller subarrays, recursively sorts them, and then merges them back to gether in sorted order.
# It is very efficient sorting algorithm in terms of time and space complexity.
# It is also stable. One down side is that it is not sorting in-place, which means that it requires additional memory for merging.

# The merge sort pseudocode example below describes important aspects on how to implement it.

# function merge(left, right):
#     result = empty array
#     while left and right are not empty:
#         if left[0] ≤ right[0]:  # Change to ≥ for descending order
#             append left[0] to result
#             remove left[0] from left
#         else:
#             append right[0] to result
#             remove right[0] from right
#     append remaining elements of left and right to result
#     return result

# function mergeSort(array):
#     if size of array ≤ 1:
#         return array
#     mid = size of array // 2
#     left = mergeSort(array[0:mid])
#     right = mergeSort(array[mid:])
#     return merge(left, right)

# Expected interface for the algorithm:

# def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
#     return None

# def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
#     # Sort PValues.
#     # PAsc: in ascending order by default. False will sort in descending order.
#     return None
# Commands:

# # Tab 1 - Insert dataset name 'A10_D10.txt' manually
# python A10_T4.py 
# # Tab 2 - CLI Argument (sys.argv[1])
# python A10_T4.py A10_D10.txt
# # Tab 3 - CLI Argument (sys.argv[1])
# python A10_T4.py A10_D100.txt
# Example program runs:

# Program starting.
# Insert filename: A10_D10.txt
# Raw 'A10_D10.txt' -> 1000, 221, 392, 621, 47, 448, 163, 120, 197, 781
# Ascending 'A10_D10.txt' -> 47, 120, 163, 197, 221, 392, 448, 621, 781, 1000
# Descending 'A10_D10.txt' -> 1000, 781, 621, 448, 392, 221, 197, 163, 120, 47

# Example merge sort solution contains 40 lines of code.

import sys
import os
from typing import List

# --- Merge Sort Implementation ---

def merge(PLeft: List[int], PRight: List[int], PMerge: List[int], PAsc: bool = True) -> None:
    """Merges two sorted lists (PLeft and PRight) into PMerge."""
    i = j = k = 0
    
    while i < len(PLeft) and j < len(PRight):
        
        # Comparison logic based on ascending or descending order
        # Ascending: True if PLeft[i] <= PRight[j]
        # Descending: True if PLeft[i] >= PRight[j]
        
        comparison = PLeft[i] <= PRight[j] if PAsc else PLeft[i] >= PRight[j]
        
        if comparison:
            PMerge[k] = PLeft[i]
            i += 1
        else:
            PMerge[k] = PRight[j]
            j += 1
        k += 1

    # Append remaining elements
    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1
    
    return None

def mergeSort(PValues: List[int], PAsc: bool = True) -> None:
    """Recursively sorts PValues using the merge sort algorithm."""
    if len(PValues) > 1:
        mid = len(PValues) // 2
        
        # Create subarrays (additional memory required)
        left = PValues[:mid]
        right = PValues[mid:]
        
        # Recursively sort the two halves
        mergeSort(left, PAsc)
        mergeSort(right, PAsc)
        
        # Merge the sorted halves back into PValues
        merge(left, right, PValues, PAsc)
        
    return None

# --- File and Display Utilities ---

def readFileContent(PFilename: str) -> List[int]:
    data = []
    try:
        if not os.path.exists(PFilename):
            raise FileNotFoundError
            
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
    
    # Handle CLI Arguments (len(sys.argv) == 2)
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        # Manual Input
        filename = input("Insert filename: ")
        
    # Read Values
    raw_data = readFileContent(filename)
    
    if not raw_data:
        print("No data loaded. Program ending.")
        sys.exit(0)
        
    # Create copies for sorting
    data_asc = raw_data[:]
    data_desc = raw_data[:]
    
    # 1. Display Raw Data
    displayData("Raw", filename, raw_data)
    
    # 2. Ascending Sort and Display
    mergeSort(data_asc)
    displayData("Ascending", filename, data_asc)
    
    # 3. Descending Sort and Display
    mergeSort(data_desc, PAsc=False)
    displayData("Descending", filename, data_desc)
    
    print("Program ending.")

if __name__ == "__main__":
    main()