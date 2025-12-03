########################################################
# Task A10_T7
# Developer Joonas Viberg
# Date 2025-12-01
########################################################

# Minesweeper is a classic puzzle game where player uncovers tiles on a grid while avoiding hidden mines.
# The goal is to clear the board by revealing all non-mine tiles or flagging all mines without triggering one.
# The entire Minesweeper game can be implemented in approximately 500 lines of Python or JavaScript code, depending on the approach and complexity. This exercise aims to guide you on this journey by introducing the first step of game development, which is the board creation (~150 lines of code).

# Design three Python functions to create a minefield for the Minesweeper game:

# """
# Ready minefield below
# [
#   [9, 3, 9, 3, 1, 0], # row 1
#   [1, 3, 9, 9, 1, 0], # row 2
#   [1, 2, 3, 2, 1, 0], # row 3
#   [1, 9, 1, 0, 1, 1], # row 4
#   [2, 3, 2, 1, 1, 9], # row 5
#   [9, 2, 9, 1, 1, 1], # row 6
#   [1, 2, 1, 1, 0, 0]  # row 7
# ]

# Numbers:
# 0 - zero nearby mines
# 1 - one nearby mine
# 2 - two nearby mines
# 3 - three nearby mines
# 4 - four nearby mines
# 5 - five nearby mines
# 6 - six nearby mines
# 7 - seven nearby mines
# 8 - eight nearby mines
# 9 - mine
# """
# import random
# random.seed(1234)

# def layMines(PMineField: list[list[int]], PMines: int):
#     """
#     The "PMineField" is pre-initialized 2d matrix with zeros.
#     [
#         [0, 0, 0, 0, 0, 0], # row 1
#         [0, 0, 0, 0, 0, 0], # row 2
#         [0, 0, 0, 0, 0, 0], # row 3
#         [0, 0, 0, 0, 0, 0], # row 4
#         [0, 0, 0, 0, 0, 0], # row 5
#         [0, 0, 0, 0, 0, 0], # row 6
#         [0, 0, 0, 0, 0, 0]  # row 7
#     ]
#     Randomly places mines to the PMineField.
#     [
#         [9, 0, 9, 0, 0, 0], # row 1
#         [0, 0, 9, 9, 0, 0], # row 2
#         [0, 0, 0, 0, 0, 0], # row 3
#         [0, 9, 0, 0, 0, 0], # row 4
#         [0, 0, 0, 0, 0, 9], # row 5
#         [9, 0, 9, 0, 0, 0], # row 6
#         [0, 0, 0, 0, 0, 0]  # row 7
#     ]
#     """
#     return None

# def calculateNearbys(PMineField: list[list[int]]) -> None:
#     """
#     Expects 2d-matrix with mines layed:
#     [
#         [9, 0, 9, 0, 0, 0], # row 1
#         [0, 0, 9, 9, 0, 0], # row 2
#         [0, 0, 0, 0, 0, 0], # row 3
#         [0, 9, 0, 0, 0, 0], # row 4
#         [0, 0, 0, 0, 0, 9], # row 5
#         [9, 0, 9, 0, 0, 0], # row 6
#         [0, 0, 0, 0, 0, 0]  # row 7
#     ]

#     Calculates nearby mines:
#     [
#         [9, 3, 9, 3, 1, 0], # row 1
#         [1, 3, 9, 9, 1, 0], # row 2
#         [1, 2, 3, 2, 1, 0], # row 3
#         [1, 9, 1, 0, 1, 1], # row 4
#         [2, 3, 2, 1, 1, 9], # row 5
#         [9, 2, 9, 1, 1, 1], # row 6
#         [1, 2, 1, 1, 0, 0]  # row 7
#     ]
#     """
#     return None

# def generateMinefield(
#         PMineField: list[list[int]],
#         PRows: int,
#         PCols: int,
#         PMines: int) -> None:
#     """
#     Takes empty "PMineField" list and amount of rows, columns and mines as parameters.
#     1. Clear 2D-Matrix
#     2. Initializes "PMineField" list with zeros using PRows and then PCols
#         for i in range(PRows): # ...
#             PMineField.append([])
#             for _ in range(PCols):
#                 PMineField[i].append(0)
#     3. Lay mines
#     4. Calculate nearbys
#     """
#     return None

# def main() -> None:
#     """
#     Create a menu-driven program where user can generate boards for the
#     Minesweeper game.

#     Option 1: Generate minesweeper board
#         - Ask amount of rows, columns and mines
#         - Create board and store into memory
#     Option 2: Show generated board
#     Option 3: Save board
#         - Ask filename and save values in comma-separated format (see below).
#     Option 0: Exit

#     ## Saved text file content start ##
#     9,3,9,3,1,0
#     1,3,9,9,1,0
#     1,2,3,2,1,0
#     1,9,1,0,1,1
#     2,3,2,1,1,9
#     9,2,9,1,1,1
#     1,2,1,1,0,0
#     ## Saved text file content end ##

#     Each line must end in newline character '\n'
#     """
#     return None

# main()
# You can add additional helper functions if needed,
# but the specified functions must remain in place with the provided interface and adhere to the described behaviour in the documentation.
# Functions layMines, calculateNearbys and generateMinefield will be extracted from the code and tested to ensure proper functionality and validation.

# Note! in this exercise, avoid using multiple program files. Create one python file A10_T7.py.

# Example program runs:
# Program starting.
# Options:
# 1 - Generate minesweeper board
# 2 - Show generated board
# 3 - Save generated board
# 0 - Exit
# Your choice: 1
# Insert rows: 4
# Insert columns: 6
# Insert mines: 10

# Options:
# 1 - Generate minesweeper board
# 2 - Show generated board
# 3 - Save generated board
# 0 - Exit
# Your choice: 2
# [9, 9, 9, 2, 9, 9]
# [3, 4, 4, 3, 3, 2]
# [3, 9, 3, 9, 2, 1]
# [9, 9, 3, 2, 9, 1]

# Options:
# 1 - Generate minesweeper board
# 2 - Show generated board
# 3 - Save generated board
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

# Example solution contains 142 lines of code.

import random
from typing import List, Tuple, Optional, Any
import sys

# Set the seed value as required
random.seed(1234)

# Constant for Mine representation
MINE = 9

def layMines(PMineField: List[List[int]], PMines: int) -> None:
    """Randomly places mines (9) to the PMineField without duplication."""
    
    rows = len(PMineField)
    if rows == 0:
        return
    cols = len(PMineField[0])
    
    total_cells = rows * cols
    if PMines > total_cells:
        PMines = total_cells # Avoid infinite loop if requested mines exceed board size

    mines_placed = 0
    while mines_placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        
        if PMineField[r][c] != MINE:
            PMineField[r][c] = MINE
            mines_placed += 1
            
    return None

def calculateNearbys(PMineField: List[List[int]]) -> None:
    """Calculates the number of nearby mines for all non-mine cells."""
    
    rows = len(PMineField)
    if rows == 0:
        return
    cols = len(PMineField[0])
    
    # Define the 8 possible offsets for neighbors (including diagonals)
    # [(dr, dc)]
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            
            # Skip cells that already contain a mine
            if PMineField[r][c] == MINE:
                continue
                
            mine_count = 0
            
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                
                # Check bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Check if the neighbor cell contains a mine
                    if PMineField[nr][nc] == MINE:
                        mine_count += 1
            
            # Update the current cell with the mine count
            PMineField[r][c] = mine_count
            
    return None

def generateMinefield(
        PMineField: List[List[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    """Initializes the matrix, lays mines, and calculates nearby numbers."""
    
    # 1. Clear 2D-Matrix
    PMineField.clear()
    
    # 2. Initializes "PMineField" list with zeros
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)
            
    # 3. Lay mines
    layMines(PMineField, PMines)
    
    # 4. Calculate nearbys
    calculateNearbys(PMineField)
    
    return None

def askInt(PPrompt: str, PMin: int, PMax: int) -> int:
    """Helper to collect and validate integer input within a range."""
    while True:
        try:
            val = int(input(PPrompt))
            if PMin <= val <= PMax:
                return val
            else:
                print(f"Input must be between {PMin} and {PMax}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            raise

def showBoard(PMineField: List[List[int]]) -> None:
    """Prints the generated minefield matrix."""
    if not PMineField:
        print("Board is empty. Generate a board first (Option 1).")
        return
        
    print("--- Generated Board ---")
    for row in PMineField:
        # Prints the row as a list string
        print(row)
    print("-----------------------")

def saveBoard(PMineField: List[List[int]]) -> None:
    """Saves the generated minefield to a file in comma-separated format."""
    if not PMineField:
        print("Board is empty. Generate a board first (Option 1).")
        return

    filename = input("Insert filename: ")
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            for row in PMineField:
                # Convert the list of integers to a comma-separated string
                line = ",".join(map(str, row))
                file.write(line + '\n')
        print(f"Board successfully saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving file: {e}")

def showMenu() -> None:
    print("\nOptions:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    
    minefield: List[List[int]] = []
    
    while True:
        try:
            showMenu()
            choice = askInt("Your choice: ", 0, 3)

            if choice == 1:
                print("--- Board Generation ---")
                rows = askInt("Insert rows: ", 1, 50)
                cols = askInt("Insert columns: ", 1, 50)
                max_mines = rows * cols
                mines = askInt("Insert mines: ", 1, max_mines)
                
                generateMinefield(minefield, rows, cols, mines)
                print("Board generated successfully.")
                
            elif choice == 2:
                showBoard(minefield)
                
            elif choice == 3:
                saveBoard(minefield)
                
            elif choice == 0:
                print("Exiting program.")
                break
                
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
    print("Program ending.")

if __name__ == "__main__":
    main()