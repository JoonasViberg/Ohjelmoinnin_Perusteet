# Create a Python program which prompts user to insert two integers.
# Use these integers together with the “for-loop” structure
# to create behaviour like in the example program example run below.
#
# Note! the autograding tool will test that the correct structure has been applied.



# Program starting.
print("Program starting.")

# Insert starting value: 1
start = int(input("\nInsert starting value: "))
# Insert stopping value: 10
stop = int(input("Insert stopping value: "))

# Starting for-loop:
print("\nStarting for-loop:")
for i in range(start, stop + 1):    
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#
# Program ending.
print("\nProgram ending.")
