# https://en.wikipedia.org/wiki/Hexagon

# Create menu-driven Python program, which can create squares, circles and hexagons. Focus of this assignment is in the creation of regular hexagons.

# Start the process of creating hexagon by prompting the user to set the center point. In SVGs, points are calculated from the top left corner.


# After center point has been collected, prompt the user again to insert apothem length.
# Use the apothem length to calculate the circumradius. Then calculate each hexagon corner point.
# Example solution calculates corners using math library’s .cos, .sin and .radians member functions.
# Start defining points from the top right corner point and move clockwise.

# Points to draw in order:

# Top Right
# Right
# Bottom Right
# Bottom Left
# Left
# Top Left


# Math terminology and formulas:

# : apothem or inradius (minimal radius)
# : circumradius (maximal radius)
# : side length




# See more details: https://www.gigacalculator.com/calculators/hexagon-calculator.php

# Polygon:

# The recommended svgwrite tool to create this shape is Polygon.
# Before applying points to the polygon shape, round the values into integers round(Value).

# Example points for hexagon with 60 inradius and center point (75, 75):

# Points = [
#     (109, 15),  # 109.64, 15.0
#     (144, 75),  # 144.28, 75.0
#     (110, 135), # 109.64, 135.0
#     (40, 135),  # 40.36, 135.0
#     (6, 75),    # 5.72, 75.0
#     (40, 15)    # 40.36, 15.0
# ]
# Apply also fill and stroke colors to the shape.

# Example program runs:

# Program starting.
# Options:
# 1 - Draw square
# 2 - Draw circle
# 3 - Draw hexagon
# 4 - Save svg
# 0 - Exit
# Your choice: 3
# Insert hexagon details:
# Middle point X: 75
# Middle point Y: 75
# Apothem length: 60
# Insert fill: antiquewhite
# Insert stroke: gray

# Options:
# 1 - Draw square
# 2 - Draw circle
# 3 - Draw hexagon
# 4 - Save svg
# 0 - Exit
# Your choice: 4
# Insert filename: A8_T7_F1.svg
# Saving file to "A8_T7_F1.svg"
# Proceed (y/n)?: y
# Vector saved successfully!

# Options:
# 1 - Draw square
# 2 - Draw circle
# 3 - Draw hexagon
# 4 - Save svg
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

from svgwrite import Drawing
import drawLib
from typing import Optional

# Import the core drawing functions
from drawLib import drawSquare, drawCircle, drawHexagon, saveSvg

def showOptions() -> None:
    """Displays the menu options."""
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    """Prompts for and validates menu choice."""
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 4.")
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
    
    drawCircle(PDwg, centerX=centerX, centerY=centerY, radius=radius, color=fill_color, stroke=stroke_color)
    print("Circle added to drawing.")

def handleDrawHexagon(PDwg: Drawing) -> None:
    """Collects parameters and calls drawHexagon."""
    print("Insert hexagon details:")
    centerX = askFloatValue("Middle point X: ")
    centerY = askFloatValue("Middle point Y: ")
    apothem = askFloatValue("Apothem length: ")
    fill_color = input("Insert fill: ")
    stroke_color = input("Insert stroke: ")
    
    drawHexagon(PDwg, centerX=centerX, centerY=centerY, apothem=apothem, fill_color=fill_color, stroke_color=stroke_color)
    print("Hexagon added to drawing.")


def main() -> None:
    print("Program starting.")
    
    dwg = Drawing(filename='default.svg', profile='tiny') 

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            handleDrawSquare(dwg)
        
        elif choice == 2:
            handleDrawCircle(dwg)
            
        elif choice == 3:
            handleDrawHexagon(dwg)
            
        elif choice == 4:
            saveSvg(dwg)
            
        elif choice == 0:
            print("Exiting program.")
            break
        
    print("Program ending.")

if __name__ == "__main__":
    main()