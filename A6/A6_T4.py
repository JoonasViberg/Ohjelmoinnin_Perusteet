# Create a program which can analyse numbers in a text file.

# Required values in analysis:

# 1 Total - integer - Sum of numbers
# 2 Count - integer - Rows that contain values
# 3 Greatest - integer - The greatest number of them all
# 4 Average - decimal - The numbers average

# Let the user specify the filename for the analysis. Program reads the file and prints the results from the analysis.
# Values must be presented like shown in the example program runs. Average name length must be presented in 2 decimal precision.
# Use Format Specification Mini-Language to achieving the required precision for the data presentation.

# Note! Given text files may contain empty rows and the program must be able to skip them if present.

# Other tips:

# Read text file line-by-line.
# Pay attention to the reading process (newline characters).
# Names can be stored into a single string variable.
# Consider separating names with a semicolon ;
# John;Doe;Jane
# Report can be stored into one string variable.
# Format Specification Mini-Language.
# E.g., "Value in 2 decimal precision {:.2f}".format(3.555)

# Example program runs

# Program starting.
# This program analyses a list of names from a file.
# Insert filename to read: A6_T4_D1.txt
# Reading names from "A6_T4_D1.txt".
# Analysing names...
# Analysis complete!
# #### REPORT BEGIN ####
# Name count - 2
# Shortest name - 3 chars
# Longest name - 4 chars
# Average name - 3.50 chars
# #### REPORT END ####
# Program ending.

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    
    print(f'Reading names from "{filename}".')
    names = []
    with open(filename, 'r') as file:
        for line in file:
            name = line.strip()
            if name:  # Skip empty lines
                names.append(name)
    
    print("Analysing names...")
    if names:
        name_lengths = [len(name) for name in names]
        count = len(names)
        shortest = min(name_lengths)
        longest = max(name_lengths)
        average = sum(name_lengths) / count
    else:
        count = 0
        shortest = 0
        longest = 0
        average = 0.0
    
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print(f"Average name - {average:.2f} chars")
    print("#### REPORT END ####")
    
    print("Program ending.")

if __name__ == "__main__":
    main()