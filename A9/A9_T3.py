########################################################
# Task A9_T3
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# Write a small Python program which read a text file.
# If the file doesn’t exist, the program must print error message to the user and the program must exit with code 1.
# Otherwise print the file content and continue program run normally.

# Test file
# A9_T3_D1.txt
# Example program runs:
# Program starting.
# Insert filename: A9_T3_D1.txt
# ## A9_T3_D1.txt ##
# File
# exists
# ## A9_T3_D1.txt ##
# Program ending.

import sys

def main() -> None:
    print("Program starting.")
    
    filename = input("Insert filename: ")
    
    try:
        with open(filename, 'r') as file:
            print(f"## {filename} ##")
            print(file.read().strip())
            print(f"## {filename} ##")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
        
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        sys.exit(1)
    
    print("Program ending.")

if __name__ == "__main__":
    main()