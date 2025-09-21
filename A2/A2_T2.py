# Make a Python program, which prompts user for a car brand and model. 
# After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters


# Program starting.

print("Program starting.")

# Insert car brand: Toyota

CarBrand = input("Insert car brand: ")

# Insert car model: Corolla

CarModel = input("Insert car model: ")

# Car brand is "Toyota" and the model is 'Corolla'.

print(f"Car brand is \"{CarBrand}\" ", end="")
print("and the model is ", f"{CarModel}'.", sep="'")

# Program ending.

print("Program ending.")