########################################################
# Task A9_T2
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# Prompt the user to insert exit code. Exit the program with using sys.exit and the user defined exit code.
# Remember to convert the value into an integer. sys.exit expects value between 0-255.

# sys.exit usage:

# import sys

# sys.exit(0) # Success exit code
# sys.exit(1) # Error exit code
# Example program runs:
# Program starting.
# Insert exit code(0-255): 0
# Clean exit

# Example solution contains 18 lines of code.

import sys

def main() -> None:
    print("Program starting.")
    
    while True:
        try:
            exit_code_input = input("Insert exit code (0-255): ")            
            exit_code = int(exit_code_input)
           
            if 0 <= exit_code <= 255:
                break
            else:
                print("Error: Exit code must be between 0 and 255.")
                
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    sys.exit(exit_code)

if __name__ == "__main__":
    main()

