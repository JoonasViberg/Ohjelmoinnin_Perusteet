# Create a menu-driven Python program with following options:
#
# Insert a word
# Which stores user inserted word into memory.
#
# Show current word
# Prints the word from the memory
#
# Show current word in reverse
# Prints the word from the memory in reverse.
#
# Exit
# Stops the program gracefully
#
# Unknown option
# Initialize the Word with an empty string.
#
# Example program runs


# Program starting.

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit

def showOptions() -> None:
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
# Your choice: 1
# Insert word: Banana
def askChoice() -> int:
    Choice = int(input("Your choice: "))
    if 0 <= Choice <= 3:
        return Choice
    else:
        print("Option is not available.")
        return -1
def main():
    Choice = -1
    Word = ""
    print("Program starting.")
    while Choice != 0:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Word = str(input("Insert word: "))
        elif Choice == 2:
            print(f'Current word - "{Word}"')
        elif Choice == 3:
            print(f'Word reversed - "{Word[::-1]}"')
    print("Exiting program. \n")
    print("Program ending.")
main()
# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 2
# Current word - "Banana"
#
# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 3
# Word reversed - "ananaB"
#
# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 0
# Exiting program.
#
# Program ending.
