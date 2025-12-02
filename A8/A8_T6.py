# Use svgwrite==1.4.3 library or build your own custom library to draw SVGs(Scalable Vector Graphics).

# Links to get started with svgwrite

# Latest svgwrite documentation: https://svgwrite.readthedocs.io/en/latest/
# Package in Pypi: https://pypi.org/project/svgwrite/
# Create menu-driven program with following options:

# Draw square (rectangle with both sides same length)
# Draw circle
# Save svg
# Exit
# Start the program creation by initialising Drawing and then define functions to fill in the details. Remember, passing object in Python works as reference to the memory.

# from svgwrite import Drawing, cm
# from svgwrite.shapes import Rect, Circle, Polygon

# def drawSquare(PDwg: Drawing) -> None:
#     # ...
#     PDwg.add(Rect(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#rect
#     return None

# def drawCircle(PDwg: Drawing) -> None:
#     # ...
#     PDwg.add(Circle(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#circle
#     return None

# def saveSvg(PDwg: Drawing) -> None:
#     # See Drawing.save method https://svgwrite.readthedocs.io/en/latest/classes/drawing.html?highlight=save#svgwrite.drawing.Drawing.save
#     return None

# def main() -> None:
#     # 1. Initialise
#     Dwg = svgwrite.Drawing()
#     # ...
#         drawSquare(Dwg)
#         drawCircle(Dwg)
#     # 3. Cleanup
#     return None

# Make the program save the created .svg in pretty format with 2 space indentations.
# Before saving, ensure the write operation from user by repeating the filename to write and then ask to proceed (y/n).

# Example program runs:

# Program starting.
# Options:
# 1 - Draw square
# 2 - Draw circle
# 3 - Save svg
# 0 - Exit
# Your choice: 1
# Insert square
# - Left edge position: 10
# - Top edge position: 10
# - Side length: 130
# - Fill color: blue
# - Stroke color: gray

# Options:
# 1 - Draw square
# 2 - Draw circle
# 3 - Save svg
# 0 - Exit
# Your choice: 3
# Insert filename: A8_T6_D1.svg
# Saving file to "A8_T6_D1.svg"
# Proceed (y/n)?: y
# Vector saved successfully!

# Options:
# 1 - Draw square
# 2 - Draw circle
# 3 - Save svg
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

from svgwrite import Drawing
import drawLib
from typing import Optional

# Import the core drawing functions
from drawLib import drawSquare, drawCircle, saveSvg

def showOptions() -> None:
    """Displays the menu options."""
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    """Prompts for and validates menu choice."""
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def askFloatValue(PPrompt: str) -> float:
    """Prompts for and validates a floating-point value."""
    while True:
        try:
            value = float(input(PPrompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def handleDrawSquare(PDwg: Drawing) -> None:
    """Collects parameters and calls drawSquare."""
    print("Insert square")
    left = askFloatValue("- Left edge position: ")
    top = askFloatValue("- Top edge position: ")
    sideLength = askFloatValue("- Side length: ")
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")
    
    # Call the library function
    drawSquare(PDwg, left=left, top=top, sideLength=sideLength, color=fill_color, strokeColor=stroke_color)
    print("Square added to drawing.")

def handleDrawCircle(PDwg: Drawing) -> None:
    """Collects parameters and calls drawCircle."""
    print("Insert circle")
    centerX = askFloatValue("- Center X position: ")
    centerY = askFloatValue("- Center Y position: ")
    radius = askFloatValue("- Radius: ")
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")
    
    # Call the library function
    drawCircle(PDwg, centerX=centerX, centerY=centerY, radius=radius, color=fill_color, stroke=stroke_color)
    print("Circle added to drawing.")

def main() -> None:
    print("Program starting.")
    
    # 1. Initialise Drawing object
    # Default units are pixels (px), which is suitable here.
    dwg = Drawing(filename='default.svg', profile='tiny') 

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            handleDrawSquare(dwg)
        
        elif choice == 2:
            handleDrawCircle(dwg)
            
        elif choice == 3:
            # The library function handles the input and confirmation
            saveSvg(dwg)
            
        elif choice == 0:
            print("Exiting program.")
            break
        
    print("Program ending.")

if __name__ == "__main__":
    main()