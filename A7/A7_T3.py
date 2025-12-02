# In this task, create a program that reads timestamps from a textfile.
# The file content is in “.csv” format and contains information related to electricity usage.

# CSV format:

# Has header row
# Columns
# Weekday
# Hour
# Consumption(kWh)
# Price(€/kWh)
# Separator ;
# Download the datasets to your computer and set up the following steps in your program:

# Prompt user to insert the filename
# Read the specified file
# Skip header row
# Read line and remove newline character
# If line is empty (contains only newline character), skip line
# Analyse timestamps per weekday
# Count each row that starts with weekday (Row.startswith(…))
# Display results
# When analysing and creating results, the recommendation is to pass the data rows and the results list to the analyse function.
# This analyse function then reads the datarows, does the calculations and fills the results list when needed.

# Displaying the results could be a function that simply iterates through the results and displays them.
# Below is a code example that can help structure the code for the task.

# WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

# def readFile(PFilename: str, PRows: list[str]) -> None:
#     print('Reading file "{}".'.format(PFilename))
#     # 0. Clear PRows list just in case
#     # 1. Open filehandle
#     # 2. Read filehandle line-by-line
#     # 2.1. Skip first line (header row)
#     # 2.2. Check if line is empty '\n'
#     # 2.3. Add non empty datarow without newline at the end.
#     # 3. Close filehandle 
#     return None

# def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
#     print("Analysing timestamps.")
#     # Append results to the PResults list
#     # Initialise helper list 
#     # WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
#     # Iterate rows with i
#     #   Iterate WEEKDAYS with j
#     #      Check if the row starts with the weekday name
#     #          Count the day in proper place
#     # Iterate WEEKDAYS with i and append the daily results
#     # Clear the helper list
#     return None

# def displayResults(PResults: list[str]) -> None:
#     print("Displaying results.")
#     # Iterate results and print for the user
#     return None

# def main() -> None:
#     # 1. Initialise
#     # 1.1. Initialise rows list
#     # 1.2. Initialise results list
#     # 2. Operate
#     # 2.1. Ask user to define filename
#     # 2.2. Read file
#     # 2.3. Analyse rows
#     # 2.3. Display results
#     # 3. Cleanup
#     # 3.1. Clear lists
#     return None

# main()

# Preferred datastructures:

# WEEKDAYS: tuple[str]
# Rows: list[str]
# Results: list[str]
# You may run the program with single bash command:

# echo -e "A7_T3_D1.csv\n" | python A7_T3.py

# Example program run:

# Program starting.
# Insert filename: A7_T3_D1.csv
# Reading file "A7_T3_D1.csv".
# Analysing timestamps.
# Displaying results.
# ### Timestamp analysis ###
#  - Monday 24 stamps
#  - Tuesday 24 stamps
#  - Wednesday 0 stamps
#  - Thursday 0 stamps
#  - Friday 0 stamps
#  - Saturnday 0 stamps
#  - Sunday 0 stamps
# ### Timestamp analysis ###
# Program ending.

def main() -> None:
    print("Program starting.")
    
    WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
    
    rows: list[str] = []
    results: list[str] = []
    
    filename = input("Insert filename: ")
    
    def readFile(PFilename: str, PRows: list[str]) -> None:
        print(f'Reading file "{PFilename}".')
        with open(PFilename, 'r') as file:
            next(file)  # Skip header row
            for line in file:
                line = line.rstrip()
                if line:  # Skip empty lines
                    PRows.append(line)
        return None
    
    def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
        print("Analysing timestamps.")
        weekday_count: dict[str, int] = {day: 0 for day in WEEKDAYS}
        
        for row in PRows:
            for day in WEEKDAYS:
                if row.startswith(day):
                    weekday_count[day] += 1
        
        PResults.append("### Timestamp analysis ###")
        for day in WEEKDAYS:
            PResults.append(f" - {day} {weekday_count[day]} stamps")
        PResults.append("### Timestamp analysis ###")
        return None
    
    def displayResults(PResults: list[str]) -> None:
        print("Displaying results.")
        for result in PResults:
            print(result)
        return None
    
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    
    rows.clear()
    results.clear()
    
    print("Program ending.")

if __name__ == "__main__":
    main()