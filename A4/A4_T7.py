# Create program which prompts the user to insert an integer 
# and then display the steps to calculate the multiplicative persistency based on the user input.
# In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. 
# This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.
#
# The program must stop the iteration when the result contains only one digit. 
# Finally before the program closes, it shows the steps taken.


# Program starting.
print("Program starting.\n")
#
# Check multiplicative persistence.
print("Check multiplicative persistence.")
# Insert an integer: 277777788888899
number = str(input("Insert an integer: "))
number_len = len(number)
step_count = 0
while len(number) > 1:
    step_count += 1
    product = 1
    for i in range(number_len):
        if i < number_len - 1:
            product = product * int(number[i])
            print(number[i], "*", end=" ")
        else:
            product = product * int(number[i])
            print(number[i], end=" ")
    number = product
    print("=", number)
    number = str(number)
    number_len = len(number)
# No more steps.
print("No more steps.")
# This program took 11 step(s)
print(f"\nThis program took {step_count} step(s)")

# Program ending.
print("\nProgram ending.")
