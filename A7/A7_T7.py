# Implement Enigma machine in Python.

# The program must handle:

# 3 x Rotors with 26 positions (A-Z)
# 1 x Reflector - Types A, B & C
# 0 x Plugboard. Prompt is required, but no need to implement.
# The order of machine operations described:

# User presses letter on the keyboard
# Keypress is passed via plugboard (skipped in this exercise)
# Rotate the wheels (positions)
# Scramble current letter using “Forward pass-through” process
# Iterate through rotors in order 1-3
# Create offset using current rotor position and the letter
# Use the offset to shift the given letter in alphabets
# Scramble current letter using using the reflector
# Scramble current letter using “Reverse pass-through” process
# Iterate through rotors in reverse order
# Change current letter based on each wheel position offset
# In this program, user inserts row and the scrambling starts always from positions [0, 0, 0]. So enter press means that the program must reset the positions before scrambling the inserted text. The Enigma machine will shut down if the user enters an empty line.

# Recommended datastructures:

# Rotors(characters): list[str]
# Positions(rotor positions): list[int]
# Reflector: str

# Initial configs

# Tab 1: iconf1.txt
# Tab 2: iconf2.txt
# Tab 3: iconf3.txt

# Rotor1:EKMFLGDQVZNTOWYHXUSPAIBRCJ
# Rotor2:AJDKSIRUXBLHWTMCQGZNPYFVOE
# Rotor3:BDFHJLCPRTXVZNYEIWGAKMUSQO
# Reflector:YRUHQSLDPXNGOKMIEBFZCWVJAT

# Example program runs

# Insert config(filename): iconf1.txt
# Insert plugs (y/n)?: n
# No extra plugs inserted.
# Enigma initialized.

# Insert row (empty stops): HELLO
# Character "H" illuminated as "E"
# Character "E" illuminated as "C"
# Character "L" illuminated as "M"
# Character "L" illuminated as "A"
# Character "O" illuminated as "M"
# Converted row - "ECMAM".

# Insert row (empty stops): ECMAM
# Character "E" illuminated as "H"
# Character "C" illuminated as "E"
# Character "M" illuminated as "L"
# Character "A" illuminated as "L"
# Character "M" illuminated as "O"
# Converted row - "HELLO".

# Insert row (empty stops): 

# Enigma closing.

# Example solution contains ~125 lines of code.

import random
import string
from typing import List, Dict

def get_config_data(filename: str) -> Dict[str, str]:
    config_data = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 4:
                config_data['Rotor1'] = lines[0].strip().split(':')[1]
                config_data['Rotor2'] = lines[1].strip().split(':')[1]
                config_data['Rotor3'] = lines[2].strip().split(':')[1]
                config_data['Reflector'] = lines[3].strip().split(':')[1]
    except FileNotFoundError:
        print(f"Error: Config file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None
    return config_data

def rotate_rotors(positions: List[int]) -> List[int]:
    
    positions[2] = (positions[2] + 1) % 26
       
    return positions

def forward_pass(char_index: int, rotors: List[str], positions: List[int]) -> int:
    ALPHABET = string.ascii_uppercase

    for i in range(3):
        # Current rotor (Rotor 1, 2, or 3)
        rotor = rotors[i]
        rotor_pos = positions[i]

        offset = rotor_pos
        
        entry_index = (char_index + offset) % 26
        
        output_char = rotor[entry_index]
        
        char_index = (ALPHABET.index(output_char) - offset) % 26
        
    return char_index

def reflector_pass(char_index: int, reflector: str) -> int:
    ALPHABET = string.ascii_uppercase
    
    input_char = ALPHABET[char_index]
    
    output_char = reflector[char_index]
    
    return ALPHABET.index(output_char)

def reverse_pass(char_index: int, rotors: List[str], positions: List[int]) -> int:
    ALPHABET = string.ascii_uppercase


    for i in range(2, -1, -1):

        rotor = rotors[i]
        rotor_pos = positions[i]

        target_char = ALPHABET[(char_index + rotor_pos) % 26]
        
        entry_index_in_rotor = rotor.index(target_char)
        
        char_index = (entry_index_in_rotor - rotor_pos) % 26
        
    return char_index

def main() -> None:
    ALPHABET = string.ascii_uppercase
    
    filename = input("Insert config(filename): ")
    config_data = get_config_data(filename)
    
    if not config_data:
        return

    rotors = [config_data['Rotor1'], config_data['Rotor2'], config_data['Rotor3']]
    reflector = config_data['Reflector']
    
    input("Insert plugs (y/n)?: ") 
    print("No extra plugs inserted.")
    print("Enigma initialized.")

    while True:

        positions = [0, 0, 0] 
        
        row_input = input("\nInsert row (empty stops): ")
        if not row_input:
            break

        row_input = row_input.upper()
        converted_row = ""

        for char in row_input:
            if char not in ALPHABET:
                converted_row += char
                continue

            char_index = ALPHABET.index(char)

            positions = rotate_rotors(positions)

            char_index = forward_pass(char_index, rotors, positions)

            char_index = reflector_pass(char_index, reflector)

            char_index = reverse_pass(char_index, rotors, positions)

            output_char = ALPHABET[char_index]
            converted_row += output_char
            
            print(f'Character "{char}" illuminated as "{output_char}"')

        print(f'Converted row - "{converted_row}".')

    print("\nEnigma closing.")

if __name__ == "__main__":
    main()