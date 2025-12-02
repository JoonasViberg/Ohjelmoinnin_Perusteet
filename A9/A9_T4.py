########################################################
# Task A9_T4
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# Create a program, which collects reasonable Celsius. Range listed below:

# TEMP_MIN = -273.15
# TEMP_MAX = 10000
# For this exercise, define collectCelsius function which returns collected celsius or raises following error:

# ValueError: "could not convert string to float: '{Feed}'"
# Exception: "{Celsius} temperature out of range."
# Example program runs:
# Program starting.
# Insert Celsius: 24
# You inserted 24.0 °C
# Program ending.

# Example solution contains 25 lines of code.

import sys

TEMP_MIN = -273.15
TEMP_MAX = 10000.0

def collectCelsius() -> float:
    raw_input = input("Insert Celsius: ")
    
    try:
        celsius = float(raw_input)
    except ValueError:
        raise ValueError("could not convert string to float: '{}'".format(raw_input))
        
    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise Exception("{} temperature out of range.".format(celsius))
        
    return celsius

def main() -> None:
    print("Program starting.")
    
    try:
        result = collectCelsius()
        print(f"You inserted {result:.1f} °C")
        
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
    print("Program ending.")

if __name__ == "__main__":
    main()