# Analyse provided CSV data and create a summary of daily power usage and cost. Use the data from the A7_T3 task. Rename files accordingly e.g., “A7_T3_D1.csv” => “A7_T5_D1.csv”.

# For the summary, calculate the daily power usage and the cost.

# Daily usage: Sum the consumption for each timestamp at the daily level. Use gatherer variable.
# Daily cost: Multiply the consumption by the daily timestamp’s corresponding price. Then sum the results into an gatherer-type variable.
# Preferred datastructures:

# Timestamps: list[TIMESTAMP]
# Analysis helper: list[DAY_USAGE]
# Results: list[str]
# Example program runs

# Program starting.
# Insert filename: A7_T5_D1.csv
# Reading file "A7_T5_D1.csv".
# Analysing timestamps.
# Displaying results.
# ### Electricity consumption summary ###
#  - Monday usage 2510.00 kWh, cost 279.42 €
#  - Tuesday usage 2364.00 kWh, cost 286.46 €
#  - Wednesday usage 0.00 kWh, cost 0.00 €
#  - Thursday usage 0.00 kWh, cost 0.00 €
#  - Friday usage 0.00 kWh, cost 0.00 €
#  - Saturnday usage 0.00 kWh, cost 0.00 €
#  - Sunday usage 0.00 kWh, cost 0.00 €
# ### Electricity consumption summary ###
# Program ending.

# Example solution contains 84 lines of code.

from dataclasses import dataclass
from typing import List, Dict

DELIMITER = ";"

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

@dataclass
class DAY_USAGE:
    weekday: str
    total_consumption: float = 0.0
    total_cost: float = 0.0

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")
day_usages: List[DAY_USAGE] = [DAY_USAGE(day) for day in WEEKDAYS]

def readTimestamps(PFilename: str, PTimestamps: List[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    try:
        with open(PFilename, 'r') as file:
            next(file)
            for line in file:
                line = line.rstrip()
                if line:
                    columns = line.split(DELIMITER) 
                    
                    if len(columns) >= 4:
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
        print(f'File "{PFilename}" not found.')
        raise

def analyseTimestamps(PTimestamps: List[TIMESTAMP], PDayUsages: List[DAY_USAGE]) -> None:
    print("Analysing timestamps.")
    
    day_gatherer: Dict[str, DAY_USAGE] = {d.weekday: d for d in PDayUsages}
    
    for timestamp in PTimestamps:
        day = timestamp.weekday
        
        if day in day_gatherer:
            daily_data = day_gatherer[day]
            
            daily_data.total_consumption += timestamp.consumption
            
            daily_data.total_cost += timestamp.consumption * timestamp.price

def displayResults(PDayUsages: List[DAY_USAGE]) -> List[str]:
    results: List[str] = []
    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for day_usage in PDayUsages:
        output = f" - {day_usage.weekday} usage {day_usage.total_consumption:.2f} kWh, cost {day_usage.total_cost:.2f} €"
        print(output)
        results.append(output)
        
    print("### Electricity consumption summary ###")
    return results

def main() -> None:
    print("Program starting.")
    
    timestamps: List[TIMESTAMP] = [] 
    
    global day_usages 
    
    filename = input("Insert filename: ")

    try:
        readTimestamps(filename, timestamps)
        
        analyseTimestamps(timestamps, day_usages)
        
        results = displayResults(day_usages)
        
    except FileNotFoundError:
        pass 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Program ending.")

if __name__ == "__main__":
    main()