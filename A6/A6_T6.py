# Create a Python program which collects plain text rows from user till the user inserts an empty row.
# Cipher all rows and then ask user to choose between showing the ciphered text or saving it.

# # English alphabets (2 x 26)
# LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
# UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Example program runs:

# Program starting.

# Collecting plain text rows for ciphering.
# Insert row(empty stops): Hello
# Insert row(empty stops): World
# Insert row(empty stops): 

# #### Ciphered text ####
# Uryyb
# Jbeyq

# #### Ciphered text ####
# Insert filename to save: A6_T6_F1.txt
# Ciphered text saved!
# Program ending.

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char: str, alphabet: str) -> str:
    """Shifts a single character by 13 positions within a given alphabet string."""

    if char in alphabet:
        index = alphabet.index(char)

        ciphered_index = (index + 13) % 26 
        return alphabet[ciphered_index]
    else:
        return char
    
def rot13(plain_text: str) -> str:
    """Ciphers a string using the ROT13 algorithm."""
    CIPHERED_TEXT = ""

    for char in plain_text:
        if char in LOWER_ALPHABETS:

            CIPHERED_TEXT += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:

            CIPHERED_TEXT += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            CIPHERED_TEXT += char

    return CIPHERED_TEXT

def writeFile(filename: str, content: list):
    """Writes a list of strings (rows) to the specified file, ensuring UTF-8 encoding."""
    with open(filename, 'w', encoding='UTF-8') as file: 
        file.write(content)

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    
    plain_text_rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        plain_text_rows.append(row)
    

    ciphered_rows = [rot13(row) for row in plain_text_rows]
    
    print("\n#### Ciphered text ####")
    for ciphered_row in ciphered_rows:
        print(ciphered_row)
    print("#### Ciphered text ####\n")
    
    filename = input("Insert filename to save: ")

    writeFile(filename, ciphered_rows)
    
    print("Ciphered text saved!")
    print("Program ending.")

if __name__ == "__main__":
    main()