# Make a menu-driven Python program which mimics Tally Counter.
#
# This menu-driven program must contain a maintainable program structure with the following requirements:
#
# main function which represents the main program logic including menu cycle.
# showOptions function which takes no arguments, shows the available options in the standard output and returns None.
# askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.
#
# In case user incorrectly inserts text as a choice, the program must output "Unknown option!".
# For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.
#
# See other requirements in the example program runs below.
#
# Example program runs



def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice() -> int:
    choice_str = input("Your choice: ").strip()

    try:
        choice = int(choice_str)
    except ValueError:
        print("Unknown option!\n")
        return -1

    if 0 <= choice <= 3:
        return choice

    print("Unknown option!\n")
    return -1  

def main():
    Count = 0
    Choice = -1

    print("Program starting.\n")

    while Choice != 0:
        showOptions()
        Choice = askChoice()

        if Choice == 1:
            print(f"Current count - {Count}\n")
        elif Choice == 2:
            Count = Count + 1
            print("Count increased!\n")
        elif Choice == 3:
            Count = 0
            print("Cleared count!\n")

    print("Exiting program.\n")
    print("Program ending.")

main()

