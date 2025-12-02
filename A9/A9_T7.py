########################################################
# Task A9_T7
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# Create a CLI tool for copying text files (similar to A6_T3). This time around, parse CLI arguments and write error handling to the program.

# A9_T7 Datasets
# A9_T7_D1.txt
# A9_T7_D2.txt
# A9_T7_D3.txt
# CLI Arguments is a new topic, and we will dive into them later in the course (extras). Python provides access to the CLI arguments via sys.argv, which is a list of strings.

# Example below illustrates how to access all CLI arguments:

# import sys

# def main() -> None:
#     print("Program starting.")
#     for i in range(len(sys.argv)):
#         print("arg_{}: {}".format(i, sys.argv[i]))
#     print("Program ending.")
#     return None

# main()
# Provide the arguments via CLI for example:

# user@host:~/projects/ohj
# $ python A9_T7.py src_file.txt dst_file.txt
# Program starting.
# arg_0: A9_T7.py
# arg_1: src_file.txt
# arg_2: dst_file.txt
# Program ending.
# user@host:~/projects/ohj
# $ 
# To check if a file exists, one could use os.path.exists-function.

# import os

# Filename = input("Insert filename: ")
# if (os.path.exists(Filename)):
#     print('File "{}" exists.'.format(Filename))
# else:
#     print('File "{}" doesn\'t exists.'.format(Filename))
# In this exercise, write the program to handle following cases(see order):

# Argument amount must be 3 (python_filename, src_file, dst_file) - if there are more or less arguments, inform user that there is invalid amount of arguments followed by the synopsis (CLI tool usage).
# Test if destination file exists (prompt user to overwrite)
# Try to open and copy files. If the operation fails, inform the user and exit program with exit code -1. Possible failure could occur if the source file doesn’t exist.
# Suggested program structures:

# import sys
# import os

# def showHelp() -> None:
#     # ...

# def copyFile(PSrcFile: str, PDstFile: str) -> None:
#     Proceed = False # One-way flag
#     if (os.path.exists(PDstFile)):
#     # ...
#     if Proceed:
#         try:

# def main() -> None:
#     # ...
#     if (len(sys.argv) == 3):
#         SrcFile = sys.argv[1]
# Example program runs:
# Program starting.
# Source file "A9_T7_D1.txt"
# Destination file "A9_T7_F1.txt"
# Copying file "A9_T7_D1.txt" to "A9_T7_F1.txt".
# Program ending.

import sys
import os

def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("Synopsis: python <python_filename> <src_file> <dst_file>")

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    Proceed = True

    if os.path.exists(PDstFile):
        print(f'File "{PDstFile}" exists.')
        confirm = input("Destination file exists. Overwrite (y/n)?: ").strip().lower()
        if confirm != 'y':
            Proceed = False
            print("Copy operation cancelled.")

    if Proceed:
        try:
            print(f'Copying file "{PSrcFile}" to "{PDstFile}".')
            
            # Check if source file exists before attempting to open
            if not os.path.exists(PSrcFile):
                raise FileNotFoundError(f"Source file '{PSrcFile}' not found.")
                
            with open(PSrcFile, 'r', encoding='UTF-8') as src:
                content = src.read()
            
            # Write to destination file
            with open(PDstFile, 'w', encoding='UTF-8') as dst:
                dst.write(content)
                
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(-1)
        except Exception as e:
            print(f"File operation failed: {e}")
            sys.exit(-1)
        
def main() -> None:
    print("Program starting.")
    
    if len(sys.argv) != 3:
        showHelp()
        # Exit with a non-zero code to indicate failure due to argument count
        sys.exit(1)
    
    # Argument count is correct (len=3: script_name, src, dst)
    SrcFile = sys.argv[1]
    DstFile = sys.argv[2]

    print(f'Source file "{SrcFile}"')
    print(f'Destination file "{DstFile}"')
    
    copyFile(SrcFile, DstFile)
    
    print("Program ending.")

if __name__ == "__main__":
    main()