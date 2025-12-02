########################################################
# Task A9_T5
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# Collect red, green and blue integer values, each on range 0-255 inclusively. This range is often described as “byte” or 8-bit.
# These 3 bytes (R, G and B) can be used to describe one color using hex notation “#rrggbb”, where the “rr” represents the amount of color red.
# The hex notation is created using the byte information.

# 28 = 162 = 255

# Above notation:

# 28 - 0-1 * 8 - 8-bits (base2)
# 162 - 0-f * 2 - Hexadecimals (base16)
# 255 - 0-9 0-255 - Integer representation (base10)

# So for example value 127(base-10) converts to 01111111(base-2) in 8-bit format or 7F(base-16) in hexadecimal format.

# While prompting values, ensure that:

# Values are numeric
# Values are actually integers
# Value is inclusively within the 0-255 range
# If any of these conditions aren’t met, then print the error message "Couldn't perform the designed task due to the invalid input values.".
# Continue the program execution to the end normally skipping the RGB displaying part.
# One way to achieve this is to use “try-except” for the whole process and then any incorrect value being collected raises exception.
# See Python Doc: Raising Exceptions

# If the RGB was ok, then show the details like in the example program run. String format specified {:02x} converts integer into 2-digit hex format.
# More details in the Python Documentation page Format Specification Mini-Language.

# Hex conversion example in Python REPL:

# >>> "#{:02x}{:02x}{:02x}".format(255, 127, 0)
# '#ff7f00'
# Example program runs:
# Program starting.
# Insert red: 255
# Insert green: 255
# Insert blue: 0
# RGB Details:
# - Red 255
# - Green 255
# - Blue 0
# - Hex #ffff00
# Program ending.
def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)

    if "." in Feed:
        raise ValueError("Input must be an integer.")

    try:
        value = int(Feed)
    except ValueError:
        raise ValueError("Input must be numeric.")

    if not (0 <= value <= 255):
        raise ValueError("Input must be in the range 0–255.")

    return value

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    red_hex = "{:02x}".format(PRed)
    green_hex = "{:02x}".format(PGreen)
    blue_hex = "{:02x}".format(PBlue)
    return f"#{red_hex}{green_hex}{blue_hex}"

def to_binary(PValue: int) -> str:
    return "{:08b}".format(PValue)

def main():
    print("Program starting.")

    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")

        hex_color = createHex(red, green, blue)
        
        # Calculate binary representations
        red_bin = to_binary(red)
        green_bin = to_binary(green)
        blue_bin = to_binary(blue)

        print("RGB Details:")
        print(f"- Red {red}, Binary {red_bin}")
        print(f"- Green {green}, Binary {green_bin}")
        print(f"- Blue {blue}, Binary {blue_bin}")
        print(f"- Hex {hex_color}")

    except ValueError as e:
        print("Couldn't perform the designed task due to the invalid input values.")
    except Exception as e:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")

if __name__ == "__main__":
    main()