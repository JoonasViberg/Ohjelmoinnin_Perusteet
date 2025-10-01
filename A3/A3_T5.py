# Create a temperature unit conversion program.

# Start the program by listing options for the user:

# Celcius to Fahrenheit
# Fahrenheit to Celcius
# Exit

# Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). 
# Lastly show the converted value to the user.

# For the unit conversions, use the formula Celcius = (Fahrenheit - 32) / 1.8

# Data representation examples:

# 50.0 °F
# 10.0 °C

# If the user chooses option Exit, notify the user: Exiting...

# Use 1 decimal precision to round the converted value.



# Program starting.

print("Program starting.\n")

# Options:

print("Options:")

# 1 - Celcius to Fahrenheit

print("1 - Celcius to Fahrenheit")

# 2 - Fahrenheit to Celcius

print("2 - Fahrenheit to Celcius")

# 0 - Exit

print("0 - Exit")

# Your choice: 1

choice = int(input("Your choice: "))

# Insert the amount of Celcius: 23

if choice == 1:
    Celcius = float(input("Insert the amount of Celcius: "))
    Fahrenheit = round((Celcius * 1.8) + 32, 1)
    print(f"{Celcius} °C equals to {Fahrenheit} °F")

# Your choice: 2

elif choice == 2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celcius = round((Fahrenheit - 32) / 1.8, 1)
    print(f"{Fahrenheit} °F equals to {Celcius} °C")

# Your choice: 0

elif choice == 0:
    print("\nExiting...")

# Your choice: Anything else

else:
    print("Unknown option.")

# Program ending.

print("\nProgram ending.")