# Make Python program which prompts user to insert two integers.
# Use these integers together with the “while-loop” structure
# to create behaviour like in the example program run below.
# Note! the autograding tool will test that the correct structure has been applied.


# Program starting.
print("Program starting.")

# Insert starting value: 1
start = int(input("\nInsert starting value: "))
# Insert stopping value: 10
stop = int(input("Insert stopping value: "))

# Starting while-loop:
print("\nStarting while-loop:")
i = start
while i <= stop:
    if i < stop:
        print(i, end=" ")
    else:
        print(i)
    i += 1
# 1 2 3 4 5 6 7 8 9 10
#
# Program ending.
print("\nProgram ending.")