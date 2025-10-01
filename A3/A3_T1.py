# Make Python program and implement if-statements in proper places.

# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two integers
# Check the parity of the sum (see modulo-operator ‘%’)



# Program starting.
print("Program starting.\n")

# Insert two integers.
print("Insert two integers.\n")

# Insert first integer: 2
Num1 = int(input("Insert first integer: "))

# Insert second integer: 3
Num2 = int(input("Insert second integer: "))

# Comparing inserted integers.
if Num1 > Num2:
    print(f"\nFirst integer is greater.\n")

# Second integer is greater.
elif Num2 > Num1:
    print(f"\nSecond integer is greater.\n")

# Adding integers together
Sum = Num1 + Num2
print(f"{Num1} + {Num2} = {Sum}\n")

# Checking the parity of the sum...
if Sum % 2 == 0:
    print("Sum is even.\n")
# Sum is odd.
else:
    print("Sum is odd.\n")

# Program ending.
print("Program ending.")
