# Create a program that can write a text file. Prompt the user to insert first name and last name.
# Then prompt the file name for the write operation. Finally write a text file with first name on the first row and last name on the second row.
# Ensure that the text file ends in a empty row. Finally exit the program cleanly.

# Example program runs

# Program starting.
# Insert first name: Guido
# Insert last name: Rossum
# Insert filename: A6_T2_F1.txt
# Program ending.

# Example written file:

# Guido
# Rossum

def main():
    print("Program starting.")
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    filename = input("Insert filename: ")
    
    with open(filename, 'w') as file:
        file.write(first_name + '\n')
        file.write(last_name + '\n')
        file.write('\n')  # Ensure the file ends with an empty row
    
    print("Program ending.")
if __name__ == "__main__":
    main()