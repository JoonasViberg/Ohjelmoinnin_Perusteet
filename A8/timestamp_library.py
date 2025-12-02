from datetime import datetime
from typing import List

# Define constants as requested
MONTHS = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"

def readTimestamps(PFilename: str, PTimestamps: List[datetime]) -> None:
    """Reads timestamps from a file and populates the PTimestamps list."""
    try:
        with open(PFilename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        # Use strptime to convert the string to a datetime object
                        dt_object = datetime.strptime(line, TIMESTAMP_FORMAT)
                        PTimestamps.append(dt_object)
                    except ValueError:
                        # Skip lines that do not match the expected format
                        continue
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        raise

def calculateYears(PYear: int, PTimestamps: List[datetime]) -> int:
    """Counts the amount of timestamps matching the given year."""
    count = 0
    for dt in PTimestamps:
        if dt.year == PYear:
            count += 1
    return count

def calculateMonths(PMonth: str, PTimestamps: List[datetime]) -> int:
    """Counts the amount of timestamps matching the given month name."""
    count = 0
    
    # Get the 1-based integer for the month (e.g., 'January' is 1)
    try:
        month_number = MONTHS.index(PMonth) + 1
    except ValueError:
        # If the month name is invalid, return 0
        return 0
        
    for dt in PTimestamps:
        if dt.month == month_number:
            count += 1
    return count

def calculateWeekdays(PWeekday: str, PTimestamps: List[datetime]) -> int:
    """Counts the amount of timestamps matching the given weekday name."""
    count = 0
    
    # Get the integer for the weekday (Monday=0, Sunday=6)
    try:
        target_weekday_index = WEEKDAYS.index(PWeekday)
    except ValueError:
        # If the weekday name is invalid, return 0
        return 0
        
    for dt in PTimestamps:
        # dt.weekday() returns Monday=0, Sunday=6
        if dt.weekday() == target_weekday_index:
            count += 1
    return count