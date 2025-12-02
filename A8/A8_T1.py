# Create a menu-driven program which has three options:

# Set pause duration
# Activate pause
# Exit
# Utilize time-library’s sleep-function to implement the pause in the program.

# Create a single program file “A8_T1.py”. Use this exercise to build the “template.py” mentioned earlier.

# Example program runs:

# Program starting.
# Options:
# 1 - Set pause duration
# 2 - Activate pause
# 0 - Exit
# Your choice: 1
# Insert pause duration (s): 0.1

# Options:
# 1 - Set pause duration
# 2 - Activate pause
# 0 - Exit
# Your choice: 2
# Pausing for 0.1 seconds.
# Unpaused.

# Options:
# 1 - Set pause duration
# 2 - Activate pause
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

import time

def main():
    print("Program starting.")
    pause_duration = 1.0
    while True:
        print("Options:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == '1':
            pause_duration = float(input("Insert pause duration (s): "))
        elif choice == '2':
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.")
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
    print("Program ending.")

if __name__ == "__main__":  
    main()