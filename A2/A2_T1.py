# Make a Python program, which prompts the user name and two floating numbers. 
# Multiply the inserted numbers to get product.
# Round the product in two decimal precision. Complete the program output as shown below

# Program starting.

print("Program starting.")

# What is your name: John

Name1 = input("What is your name: ")

# Enter a floating point number: 3.1

Number1 = float(input("Enter a floating point number: "))

# Enter second floating point number: 5.3

Number2 = float(input("Enter second floating point number: "))

# John you gave numbers 3.1 and 5.3

print(f"{Name1} you gave numbers {Number1} and {Number2}")

# Multiplying first and second number will result in product 16.43

Product1 = round(Number1 * Number2, 2)

print(f"Multiplying first and second number will result in product {Product1}")

# Program ending

print("Program ending.")