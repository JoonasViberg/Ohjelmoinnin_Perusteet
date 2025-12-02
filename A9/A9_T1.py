########################################################
# Task A9_T1
# Developer Joonas Viberg
# Date 2025-11-29
########################################################

# Create a Python program that prompts the user to insert floating-point values. If the user inserts 0, stop the prompt and print the sum of the inserted values.

# If the user inserts an invalid value, such as “aaaaa” or “1.b2”, print an error message indicating that the inserted value couldn’t be converted to a floating-point number.
# Skip the incorrect feed and continue prompting.

# During the prompts, use the raw values for the presentation ("{}".format(Value)).
#     In the final sum presentation, use two decimal presentation format.
# This can be achieved by using the float format specifier.

# "{:.2f}".format(Value)

# Inputs (for advanced testing):
# 3.5
# aaaaa
# 1.5
# 0

# Commands to run inputs:

# cat input1.txt | python A9_T1.py
# cat input2.txt | python A9_T1.py
# cat input3.txt | python A9_T1.py

# Example program runs:

# Program starting.

# Insert a floating-point value (0 to stop): 3.5
# Insert a floating-point value (0 to stop): aaaaa
# Error! 'aaaaa' couldn't be converted to float.
# Insert a floating-point value (0 to stop): 1.5
# Insert a floating-point value (0 to stop): 0

# Final sum is 5.00
# Program ending.

# Example solution contains 23 lines of code.

def main() -> None:
    print("Program starting.")
    
    total_sum = 0.0
    
    while True:
        prompt = "Insert a floating-point value (0 to stop): "
        raw_input = input(prompt)
        
        print(raw_input) 

        try:
            value = float(raw_input)
            
            if value == 0.0:
                break
            
            total_sum += value
            
        except ValueError:

            print("Error! '{}' couldn't be converted to float.".format(raw_input))

    print("Final sum is {:.2f}".format(total_sum))
    print("Program ending.")

if __name__ == "__main__":
    main()