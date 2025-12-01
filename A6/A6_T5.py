#Create a program which can analyse numbers in a text file.

# Required values in analysis:

# 1 sum - integer - Sum of numbers
# 2 Count - integer - Rows that contain values
# 3 Greatest - integer - The greatest number of them all
# 4 Average - decimal - The numbers average

# Think about the processes or “steps” of the analytics first. A prosess which can be described with a name should be wrapped into a function.
# This function then should only do the task, which belongs to it based on the name. For example if the function name is “readValues”, then the function should read the values from a file.
# If the function name is “analyseNumbers”, then it should not read a textfile.

# This can be difficult at first with the current know-how, because return statement can only return one value and we have not looked into the datastructures yet.
# But if you want, you can wrap the values into a string variable using separator in-between the values. This way string can contain multiple values and can be returned as a single value from a function.

# Pseudo-example below:

# SEPARATOR = ";"

# def readValues() -> str:
#   # read operations...
#   Values: str = ""
#   Values += str(13) + SEPARATOR
#   Values += str(45) + SEPARATOR
#   Values += str(20)
#   return Values

# contain only things that the Divide the program structure based on the processes.
# Define functions to handle the meaningful smaller parts of the program e.g., reading numbers from a given textfiles, analysing numbers and displaying results.
# Reading values from a file and then storing the values back into a string for the return will help to separate value reading and analysis into their own functionalities.

# This task will not evaluate how well you have structured your code or separated the processes into their own functionalities.
# But definitely this is a good place to start to consider how robust code are you actually building.

# Present average result in 2 digit precision. Utilize the Format Specification Mini-Language.

# Syntax for 2 digit precision: '{:.2f}'

# Dataset details:

# These datasets contain only positive integer numbers.
# No empty lines. POSIX Line definition
# The results are displayed in CSV format in the example program runs. The first row contains headers, followed by a single data row.
# Both the column headers and the data values are separated by a semicolon (;).
# The format is similar to how data is structured in Excel.

# Count	Sum	Greatest	Average
# 2	53 43   26.50

# Example program runs

# run 1 run 2 run 3
# Program starting.
# Insert filename: A6_T5_D1.txt
# #### Number analysis - START ####
# File "A6_T5_D1.txt" results:
# Count;Sum;Greatest;Average
# 2;53;43;26.50

# #### Number analysis - END ####
# Program ending.

def readValues(filename: str) -> list:

    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                # Check if the line contains only digits
                if line.isdigit():
                    numbers.append(int(line))
        return numbers
    except FileNotFoundError:
        print(f"ERROR: File not found: {filename}")
        return []

def analyseValues(numbers: list) -> str:

    total = sum(numbers)
    count = len(numbers)
    # Get the greatest number or 0 if the list is empty
    greatest = max(numbers) if numbers else 0
    # Calculate average safely, or 0 if the count is zero
    average = total / count if count > 0 else 0

    
    return 'Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n'.format(
        count=count,
        total=total,
        greatest=greatest,
        average=average
    )


def main():

    print("Program starting.")
    

    filename = input("Insert filename: ")
    
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    
    numbers = readValues(filename)
    
    results = analyseValues(numbers)
    print(results)

    print("#### Number analysis - END ####")
    print("Program ending.")
    
if __name__ == "__main__":
    main()