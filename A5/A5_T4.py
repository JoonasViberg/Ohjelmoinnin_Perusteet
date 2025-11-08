# The following code should calculate the area of a rectangle based on the user inputs.
# Fix the example code below without altering defined function names or function parameters.
# Fixed code must produce similar results as is in the expected program runs.
# The code must also be fixed to match the requirements in the provided style guide.

# def askDimension(PPrompt: str) -> float:
#    Feed = input("Insert number: ")
#    return Feed



# Width = askNumber("width")
# Height = askNumber("height")

# def calcRectangleArea(PWidth: float, PHeight: float) -> float:
#    PWidth = Area * PHeight
#    return Sum

# Area = calculateArea()
# print("")
# print("Area is {Area}²")
# print("end")

# Program starting.
print("Program starting.")
# Insert width: 2
def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed
# Insert height: 3
def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Width = askDimension("width")
Height = askDimension("height")
Area = calcRectangleArea(Width, Height)
#
# Area is 6.0²
print("")
print(f"Area is {Area}²")
# Program ending.
print("Program ending.")







