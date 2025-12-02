# Create a Python program that processes a list of comma-separated integers entered by the user.

# Insert comma separated integers: 2,2,1,3,12,8

# The program will perform the following operations:

# Parse the input, validate that all entries are valid integers.
# If an invalid value is detected, output an error message indicating the invalid value, but still process the valid integers.
# Calculate the sum of the valid integers and determine if the sum is even or odd.
# Display the total count of valid integers, the sum of the integers, and whether the sum is even or odd.
# If no valid integers are provided, display an appropriate message.
# Requirements:

# Input:
# The user inputs a comma-separated list of values.
# The program parses these the entered values and checks if they are valid.
# Output:
# If all values are valid, display the number of integers, their sum, and whether the sum is even or odd.
# If invalid values have been entered, display an error message for the invalid value.
# If no valid integers remain after parsing, inform the user that there are no values to analyze.
# Preferred datastructures: list[int]

# Example program runs

# Program starting.
# Insert comma separated integers: 2,2,1,3
# There are 4 integers in the list.
# Sum of the integers is 8 and it's even
# Program ending.

# Example solution contains 44 lines of code.

def main() -> None:
    print("Program starting.")
    
    user_input = input("Insert comma separated integers: ")
    entries = user_input.split(',')
    
    valid_integers: list[int] = []
    
    for entry in entries:
        entry = entry.strip()
        try:
            number = int(entry)
            valid_integers.append(number)
        except ValueError:
            print(f'Invalid value "{entry}" detected.')
    
    if valid_integers:
        total_count = len(valid_integers)
        total_sum = sum(valid_integers)
        even_odd = "even" if total_sum % 2 == 0 else "odd"
        
        print(f"There are {total_count} integers in the list.")
        print(f"Sum of the integers is {total_sum} and it's {even_odd}")
    else:
        print("No valid integers to analyze.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()