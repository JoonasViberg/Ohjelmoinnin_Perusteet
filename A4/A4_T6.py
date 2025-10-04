# Create a program which prompts the user to insert an integer
# and then display the collatz conjecture as shown in the examples below.


# Program starting.
print("Program starting.")

# Insert a positive integer: 10
number = int(input("Insert a positive integer: "))
step_count = 0
print(number, end=" ")
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1    
    step_count += 1

    # 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    if number != 1:
        print("->", number, end=" ")
    else:
        print("->", number)

# Sequence had 6 total steps.
print(f"Sequence had {step_count} total steps.")

# Program ending.
print("\nProgram ending.")
