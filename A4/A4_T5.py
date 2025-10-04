# Make a program, which prompts user to insert three integers:
#
# Starting point
# Stopping point
# Inspection point
#
# Test the points with following rules(Note! testing order matters):
#
# Starting point must be less than stopping point
# "Starting point value must be less than the stopping point value."
#
# The inspection point must be within the range of the start and stop points.
# "Inspection value must be within the range of start and stop."
#
# If any rule above is broken, print the violation message(s) to the user and then skip the next part till the "Program ending." print.
#
# Run two for-loops like shown in the example program runs if none of the rules above are broken. 
# Inside the loops, compare the inspection point to the current iteration. 
# Use break and continue commands if the current iteration is same as the inspection point. 
# Otherwise print the current iteration on the same line.
#
# Note! There must be no trailing space character at the end of any row.



# Program starting.
print("Program starting.\n")

# Insert starting point: 3
start = int(input("Insert starting point: "))
# Insert stopping point: 8
stop = int(input("Insert stopping point: "))
# Insert inspection point: 5
inspection = int(input("Insert inspection point: "))
print("")

# Test the points and print possible violation messages:
if start >= stop or inspection < start or inspection > stop:
    if start >= stop:
        print("Starting point value must be less than the stopping point value.")
    if inspection < start or inspection > stop:
        print("Inspection value must be within the range of start and stop.")
else:
    # First loop - inspection with break:
    print("First loop - inspection with break:")
    for i in range(start, stop + 1):
        if i == inspection:
            print("")
            break
        if i < stop:
            print(i, end=" ")
        else:
            print(i)

    # Second loop - inspection with continue:
    print("Second loop - inspection with continue:")
    for i in range(start, stop + 1):
        if i == inspection:
            continue
        if i < stop:
            print(i, end=" ")
        else:
            print(i)
    if stop == inspection:
        print("")
# Program ending.
print("\nProgram ending.")