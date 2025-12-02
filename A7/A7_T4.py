# Structure timestamp data in program.

# This task is continuation to the A7_T3 task. You may start this task by copying the previous datasets. Rename datasets to match this task e.g., “A7_T3_D1.csv” => “A7_T4_D1.csv”.

# The dataset had four different values separated by a semicolon ;:

# Weekday
# Hour
# Consumption(kWh)
# Price(€/kWh)
# The goal is to print each timestamp from a file and also calculate the total of consumption and price. Below is the output format for a single record.

# Electiricity usages:
# - Monday 12:00, price 0.20 €, consumption 15.00 kWh, total 3.00 €
# - ...
# To keep the code maintainable, define a named datastructure for the different values. Once defined, specify a way to read the timestamps into a list. This can be done by reading a file line by line, skipping empty lines, trimming line endings, and then splitting each line by the delimiter.

# Code example of the operations:

# # Constants
# DELIMITER = ";"
#   # iterate over lines
#     ...
#     Row = Line.rstrip()               # Remove newline
#     Columns = Row.split(DELIMITER)      # Splits the row into a list
#     Timestamp = TIMESTAMP()           # Create object
#     Timestamp.weekday = Columns[0]      # Collect the first column
#     ...                               # Collect rest of the columns...
#     Timestamp.price = float(Columns[3]) # Collect the fourth column and convert datatype
#     Columns.clear()
# Preferred datastructures:

# Timestamps: list[TIMESTAMP]
# Example program runs

# Program starting.
# Insert filename: A7_T4_D1.csv
# Reading file "A7_T4_D1.csv".
# Electricity usage:
#  - Monday 00:00, price 0.09, consumption 154.00 kWh, total 13.86 €
#  - Monday 01:00, price 0.07, consumption 125.00 kWh, total 8.75 €
#  - Monday 02:00, price 0.13, consumption 158.00 kWh, total 20.54 €
#  - Monday 03:00, price 0.12, consumption 61.00 kWh, total 7.32 €
#  - Monday 04:00, price 0.15, consumption 149.00 kWh, total 22.35 €
#  - Monday 05:00, price 0.09, consumption 69.00 kWh, total 6.21 €
#  - Monday 06:00, price 0.08, consumption 77.00 kWh, total 6.16 €
#  - Monday 07:00, price 0.07, consumption 141.00 kWh, total 9.87 €
#  - Monday 08:00, price 0.08, consumption 148.00 kWh, total 11.84 €
#  - Monday 09:00, price 0.13, consumption 90.00 kWh, total 11.70 €
#  - Monday 10:00, price 0.11, consumption 93.00 kWh, total 10.23 €
#  - Monday 11:00, price 0.05, consumption 47.00 kWh, total 2.35 €
#  - Monday 12:00, price 0.08, consumption 66.00 kWh, total 5.28 €
#  - Monday 13:00, price 0.08, consumption 66.00 kWh, total 5.28 €
#  - Monday 14:00, price 0.15, consumption 137.00 kWh, total 20.55 €
#  - Monday 15:00, price 0.15, consumption 60.00 kWh, total 9.00 €
#  - Monday 16:00, price 0.07, consumption 69.00 kWh, total 4.83 €
#  - Monday 17:00, price 0.19, consumption 136.00 kWh, total 25.84 €
#  - Monday 18:00, price 0.09, consumption 67.00 kWh, total 6.03 €
#  - Monday 19:00, price 0.19, consumption 150.00 kWh, total 28.50 €
#  - Monday 20:00, price 0.11, consumption 103.00 kWh, total 11.33 €
#  - Monday 21:00, price 0.05, consumption 136.00 kWh, total 6.80 €
#  - Monday 22:00, price 0.10, consumption 108.00 kWh, total 10.80 €
#  - Monday 23:00, price 0.14, consumption 100.00 kWh, total 14.00 €
#  - Tuesday 00:00, price 0.15, consumption 87.00 kWh, total 13.05 €
#  - Tuesday 01:00, price 0.12, consumption 58.00 kWh, total 6.96 €
#  - Tuesday 02:00, price 0.11, consumption 43.00 kWh, total 4.73 €
#  - Tuesday 03:00, price 0.13, consumption 74.00 kWh, total 9.62 €
#  - Tuesday 04:00, price 0.13, consumption 103.00 kWh, total 13.39 €
#  - Tuesday 05:00, price 0.06, consumption 88.00 kWh, total 5.46 €
#  - Tuesday 06:00, price 0.10, consumption 56.00 kWh, total 5.60 €
#  - Tuesday 07:00, price 0.08, consumption 83.00 kWh, total 6.64 €
#  - Tuesday 08:00, price 0.17, consumption 131.00 kWh, total 22.27 €
#  - Tuesday 09:00, price 0.12, consumption 69.00 kWh, total 8.28 €
#  - Tuesday 10:00, price 0.19, consumption 132.00 kWh, total 25.08 €
#  - Tuesday 11:00, price 0.10, consumption 85.00 kWh, total 8.50 €
#  - Tuesday 12:00, price 0.17, consumption 156.00 kWh, total 26.52 €
#  - Tuesday 13:00, price 0.16, consumption 45.00 kWh, total 7.20 €
#  - Tuesday 14:00, price 0.07, consumption 138.00 kWh, total 9.66 €
#  - Tuesday 15:00, price 0.12, consumption 144.00 kWh, total 17.28 €
#  - Tuesday 16:00, price 0.15, consumption 76.00 kWh, total 11.40 €
#  - Tuesday 17:00, price 0.17, consumption 63.00 kWh, total 10.71 €
#  - Tuesday 18:00, price 0.09, consumption 132.00 kWh, total 11.88 €
#  - Tuesday 19:00, price 0.08, consumption 152.00 kWh, total 12.16 €
#  - Tuesday 20:00, price 0.15, consumption 85.00 kWh, total 12.75 €
#  - Tuesday 21:00, price 0.17, consumption 92.00 kWh, total 15.64 €
#  - Tuesday 22:00, price 0.10, consumption 134.00 kWh, total 13.40 €
#  - Tuesday 23:00, price 0.06, consumption 138.00 kWh, total 8.28 €
# Program ending.

# Example solution contains 55 lines of code.

from dataclasses import dataclass
from typing import List


DELIMITER = ";"

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float  
    price: float        

def readTimestamps(PFilename: str, PTimestamps: List[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    try:
        with open(PFilename, 'r') as file:
            next(file)

            for line in file:
                line = line.rstrip()
                if line:
                    columns = line.split(DELIMITER)

                    if len(columns) < 4:
                        continue
                    
                    try:
                        timestamp = TIMESTAMP(
                            weekday=columns[0],
                            hour=columns[1],
                            consumption=float(columns[2]),
                            price=float(columns[3])
                        )
                        PTimestamps.append(timestamp)
                    except ValueError:

                        continue
    except FileNotFoundError:
        print(f"Error: File not found: {PFilename}. Please ensure the file exists and the name is correct.")
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")

def displayTimestamps(PTimestamps: List[TIMESTAMP]) -> None:

    print("Electricity usage:")
    

    if not PTimestamps:
        print("No data records found.")
        return

    for timestamp in PTimestamps:

        total = timestamp.consumption * timestamp.price
        
        print(f" - {timestamp.weekday} {timestamp.hour}, price {timestamp.price:.2f}, consumption {timestamp.consumption:.2f} kWh, total {total:.2f} €")

def main() -> None:

    print("Program starting.")
    
    timestamps: List[TIMESTAMP] = [] 
    
    filename = input("Insert filename: ")

    readTimestamps(filename, timestamps)
    
    displayTimestamps(timestamps)
    
    timestamps.clear()

    print("Program ending.")

if __name__ == "__main__":
    main()