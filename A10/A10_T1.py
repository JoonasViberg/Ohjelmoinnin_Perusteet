########################################################
# Task A10_T1
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# First download the datasets above.
# Then create a program which prompts user to insert a filename and then displays the file content in two different ways:

# Vertically - Each value on its own row.
# Horizontally - Values on the same row, separated by comma and space “, ”.
# While reading the file rows, strip the newline characters and ignore empty rows.

# Example program runs:

# Program starting.
# Insert filename: A10_D10.txt
# # --- Vertically --- #
# 1000
# 221
# 392
# 621
# 47
# 448
# 163
# 120
# 197
# 781
# # --- Vertically --- #
# # --- Horizontally --- #
# 1000, 221, 392, 621, 47, 448, 163, 120, 197, 781
# # --- Horizontally --- #
# Program ending.
# Example solution contains 52 lines of code.

from typing import List

def readFileContent(PFilename: str) -> List[str]:
    data = []
    try:
        with open(PFilename, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    data.append(line)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        # Return an empty list to signal failure without exiting the program
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return data

def displayVertically(PData: List[str]) -> None:
    print("# --- Vertically --- #")
    for item in PData:
        print(item)
    print("# --- Vertically --- #")

def displayHorizontally(PData: List[str]) -> None:
    print("# --- Horizontally --- #")
    # Use the join method to concatenate all elements with ", " separator
    print(", ".join(PData))
    print("# --- Horizontally --- #")

def main() -> None:
    print("Program starting.")
    
    filename = input("Insert filename: ")
    
    file_data = readFileContent(filename)
    
    if file_data:
        displayVertically(file_data)
        displayHorizontally(file_data)
    
    print("Program ending.")

if __name__ == "__main__":
    main()