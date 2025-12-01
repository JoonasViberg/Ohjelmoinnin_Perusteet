# Create a program that can read a text file and then print the file content. User must be able to specify the file name. Decorate the beginning and the end of the file with a decorative line.

# Decorative lines

#     #### START "{filename}" ####
#     #### END "{filename}" ####

# Example program runs

# Program starting.
# This program can read a file.
# Insert filename: A6_T1_D1.txt
# #### START "A6_T1_D1.txt" ####
# Hello
# World

# #### END "A6_T1_D1.txt" ####
# Program ending.

def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    
    print(f'#### START "{filename}" ####')
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end='')
    print(f'#### END "{filename}" ####')
    
    print("Program ending.")
if __name__ == "__main__":
    main()