# Create a Python program to convert Fahrenheit to Celcius. 
# Round the Celsius to 1 decimal precision.
# Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8


# Program starting.
print("Program starting.")

# Insert fahrenheits: 50
Fahrenheit = float(input("Insert fahrenheits: "))
Celcius = round((Fahrenheit - 32) / 1.8, 1)

# 50.0°F is 10.0°C
print(f"{Fahrenheit}°F is {Celcius}°C")

# Program ending.
print("Program ending.")
