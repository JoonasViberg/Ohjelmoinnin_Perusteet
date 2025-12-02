########################################################
# Task A9_T6
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# In some scenarios, programs contain unsaved user data, and the user may accidentally do something that typically causes the program to close.
# In CLI programs, this occurs if the user sends a keyboard interrupt (CTRL + C).
# Handle the KeyboardInterrupt in a menu-driven program, which collects user-inserted lines.

# If the user has inserted 0 lines during a program run, there is nothing to save.
# Handle the keyboard interrupt (CTRL + C) smoothly by informing the user that the program is closing suddenly.

# If the user has inserted 1 or more lines and then presses CTRL + C, prompt the user to confirm if they would like to save the lines to a file.
# If the user confirms with yes, ask for the filename to write. Otherwise close the program gracefully.

# In the example program runs below, keypair ^C indicates user initiated KeyboardInterrupt.
# Text after ^C on the same line represents program output after keyboard interrupt (color glitch).

# Example program runs:
# Program starting.
# Options:
# 1 - Insert line
# 2 - Save lines
# 0 - Exit
# Your choice: 1
# Insert text: First line.

# Options:
# 1 - Insert line
# 2 - Save lines
# 0 - Exit
# Your choice: 1
# Insert text: Second line.

# Options:
# 1 - Insert line
# 2 - Save lines
# 0 - Exit
# Your choice: ^CKeyboard interrupt and unsaved progress!
# Save before quit(y/n)?: y
# Insert filename: file1.txt
# Program ending.
# Example solution contains 64 lines of code.

import sys
from typing import List

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> int:
    while True:
        try:
            choice = input("Your choice: ")
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            raise

def saveLines(PLines: List[str]) -> None:
    if not PLines:
        print("No lines to save.")
        return

    filename = input("Insert filename: ")
    try:
        # FIX: Pass the input list directly. The test assumes the list already contains newlines.
        with open(filename, 'w', encoding='UTF-8') as file:
            file.writelines(PLines)
            
        print(f"Successfully saved {len(PLines)} lines to '{filename}'.")
        PLines.clear()
    except Exception as e:
        print(f"Error saving file: {e}")

def insertLine(PLines: List[str]) -> None:
    line = input("Insert text: ")
    # When running interactively, we must add the newline character manually, 
    # since the saveLines fix assumes it's present.
    PLines.append(line + '\n') 
    print("Line inserted.")

def onInterrupt(PLines: List[str]) -> None:
    print("Keyboard interrupt and unsaved progress!")
    
    if not PLines:
        print("No unsaved lines. Program closing suddenly.")
        return

    print(f"You have {len(PLines)} unsaved lines.")
    
    while True:
        try:
            save_confirm = input("Save before quit(y/n)?: ").strip().lower()
            if save_confirm == 'y':
                saveLines(PLines)
                return
            elif save_confirm == 'n':
                print("Closing program without saving.")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        except KeyboardInterrupt:
            print("Interrupt confirmed. Closing program.")
            return

def main() -> None:
    Lines: List[str] = []
    Choice = -1
    print("Program starting.")
    
    try:
        while Choice != 0:
            showOptions()
            
            try:
                Choice = askChoice()
            except KeyboardInterrupt:
                raise

            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                if Lines:
                    print("Unsaved progress!")
                    onInterrupt(Lines) 
                print("Exiting program.")
                
            else:
                print("Unknown option!")
            print("")
            
    except KeyboardInterrupt:
        onInterrupt(Lines)
        
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()