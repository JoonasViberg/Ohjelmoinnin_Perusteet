# Create menu program with submenus. Mainly for unit conversions. 
# Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

# Menu options:

# Length
# Meters to kilometers
# Kilometers to meters

# Weight
# Grams to pounds
# Pounds to grams

# Exit
# “Exiting...”

# Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

# Other possible prints:

# “Unknown option.”



# Program starting.
print("Program starting.")

# Welcome to the unit converter program!
print("Welcome to the unit converter program!")

# Follow the menu instructions below.
print("Follow the menu instructions below.\n")

# Options:
print("Options:")
# 1 - Length
print("1 - Length")
# 2 - Weight
print("2 - Weight")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
choice = int(input("Your choice: "))

# Length options:

if choice == 1:
    print("\nLength options:")
    # 1 - Meters to kilometers
    print("1 - Meters to kilometers")

    # 2 - Kilometers to meters
    print("2 - Kilometers to meters")

    # 0 - Exit
    print("0 - Exit")

    # Your choice: 1
    length_choice = int(input("Your choice: "))

    # Insert meters: 1000
    if length_choice == 1:
        meters = float(input("Insert meters: "))
        kilometers = round(meters / 1000, 1)
        print(f"{meters} m is {kilometers} km")

    # Insert kilometers: 1
    elif length_choice == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = round(kilometers * 1000, 1)
        print(f"{kilometers} km is {meters} m")

    # Exit
    elif length_choice == 0:
        print("Exiting...")
    # Unknown option
    else:
        print("Unknown option.")


# Your choice: 2

elif choice == 2:
    print("\nWeight options:")
    # 1 - Grams to pounds
    print("1 - Grams to pounds")

    # 2 - Pounds to grams
    print("2 - Pounds to grams")

    # 0 - Exit
    print("0 - Exit")

    # Your choice: 1
    weight_choice = int(input("Your choice: "))

    # Insert grams: 1000
    if weight_choice == 1:
        grams = float(input("Insert grams: "))
        pounds = round(grams / 453.6, 1)
        print(f"{grams} g is {pounds} lb")

    # Insert pounds: 2.2
    elif weight_choice == 2:
        pounds = float(input("Insert pounds: "))
        grams = round(pounds * 453.6, 1)
        print(f"{pounds} lb is {grams} g")

    # Exit
    elif weight_choice == 0:
        print("Exiting...")
    # Unknown option
    else:
        print("Unknown option.")

# Your choice: 0

elif choice == 0:
     print("Exiting...")

# Unknown option

else:
    print("Unknown option.")
# Program ending.
print("\nProgram ending.")