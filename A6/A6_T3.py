# Create a program that copies a text file by reading from a source file and writing the content to a destination file. 
# Allow the user to specify the source and destination file names.

# Example program runs

# Program starting.
# This program can copy a file.
# Insert source filename: A6_T3_D1.txt
# Insert destination filename: A6_T3_F1.txt
# Reading file 'A6_T3_D1.txt' content.
# File content ready in memory.
# Writing content into file 'A6_T3_F1.txt'.
# Copying operation complete.
# Program ending.

def main():
    print("Program starting.")
    print("This program can copy a file.")
    source_filename = input("Insert source filename: ")
    destination_filename = input("Insert destination filename: ")
    
    print(f"Reading file '{source_filename}' content.")
    with open(source_filename, 'r') as source_file:
        content = source_file.read()
    print("File content ready in memory.")
    
    print(f"Writing content into file '{destination_filename}'.")
    with open(destination_filename, 'w') as dest_file:
        dest_file.write(content)
    print("Copying operation complete.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()