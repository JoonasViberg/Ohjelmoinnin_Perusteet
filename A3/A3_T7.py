# In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. 
# Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results.
#  Structure, order and operators matter, so do exactly as the task describes.

# Prompt user to insert value as an integer.
# Display menu
# option 1 - In one multi-branched decision
# option 2 - Independent if-statement decisions
# option 0 - Exit
# Prompt user to choose option

# Apply following math operations in the options 1 & 2

# One multi-branched decision structure:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value

# Independent if-statement decisions one after another:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value

# Exit: “Exiting…”

# At the end of the options 1 & 2, show the results like in the example program runs.

# Other possible output variats:

# “Unknown option.”



# Program starting.
print("Program starting.\n")

# Testing decision structures.
print("Testing decision structures.\n")

# Insert an integer: 250
value = int(input("Insert an integer: "))

# Options:
print("\nOptions:")

# 1 - In one multi-branched decision
print("1 - In one multi-branched decision")

# 2 - In multiple independent if-statements
print("2 - In multiple independent if-statements")

# 0 - Exit
print("0 - Exit")

# Your choice: 1
choice = int(input("Your choice: "))

# Using one multi-branched decision structure.
if choice == 1:
    if value >= 400:
        value += 44
    elif value >= 200:
        value += 22
    elif value >= 100:
        value += 11
    print(f"Result is {value}")

# Using multiple independent if-statements.
elif choice == 2:
    if value >= 400:
        value += 44
    if value >= 200:
        value += 22
    if value >= 100:
        value += 11
    print(f"Result is {value}")
    
# Exit
elif choice == 0:
    print("Exiting...")  

# Unknown option
else:
    print("Unknown option.")

# Program ending.
print("\nProgram ending.")