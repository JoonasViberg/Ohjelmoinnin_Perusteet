# Create a program that collects positive integers from the user until user enters a negative integer. After this, the program should then display the collected integers along with their indices and ordinals. If no integers are entered, the program should gracefully handle the situation by displaying an appropriate message.

# Input: The program repeatedly prompt the user to enter positive integers. If the user enters a negative integer, the input process stops.
# Validation: Only positive integers should be collected. A negative integer stops the input collection.
# Output:
# After input is stopped, the program will display the collected integers.
# For each integer, show the following:
# Index (starting from 0).
# Ordinal (index + 1).
# If there are no integers, inform the user that there are no integers to display.
# Program Flow:
# The program starts with the message: “Program starting.”
# Collect positive integers from the user.
# Stop collecting on a negative number.
# After stopping input, display the results.
# The program ends with the message: “Program ending.”
# Preferred datastructures:

# list[int]
# Example program runs:

# Program starting.
# Collect positive integers.
# Insert positive integer(negative stops): 5
# Insert positive integer(negative stops): 10
# Insert positive integer(negative stops): 15
# Insert positive integer(negative stops): -1
# Stopped collecting positive integers.
# Displaying 3 integers:
# - Index 0 => Ordinal 1 => Integer 5
# - Index 1 => Ordinal 2 => Integer 10
# - Index 2 => Ordinal 3 => Integer 15
# Program ending.

def main() -> None:
    print("Program starting.")
    print("Collect positive integers.")
    
    integers: list[int] = []
    
    while True:
        user_input = input("Insert positive integer(negative stops): ")
        try:
            number = int(user_input)
            if number < 0:
                break
            integers.append(number)
        except ValueError:
            print(f'Invalid input "{user_input}". Please enter an integer.')
    
    print("Stopped collecting positive integers.")
    
    if integers:
        print(f"Displaying {len(integers)} integers:")
        for index, value in enumerate(integers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
    else:
        print("No integers to display.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()