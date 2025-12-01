# Each of the Four Emperors—Galba, Otho, Vitellius and Vespasian—has left a message in their own palaces.
# Your task is to travel programmatically to each location and gather all their messages.

# You may travel only once per program run. Travel should begin by displaying the current location, followed by the process of traveling to the next location.
# The first location is the “start” or “Home” location on the map below.

# Place names listed:

# home
# Galba's palace
# Otho's palace
# Vitellius' palace
# Vespasian's palace
# Create a file “player_progress.txt” and initialize it with the following details.

# file 1
#   current_location;next_location;passphrase
#   0;1;qvfpvcyvar

# Player progress file explained:

# First row is the header row with the column names.
# Data row 1
# Current location id 0 refers to the starting point (Home).
# Next location id 1 refers to the next objective (Galba's palace).
# Passphrase ciphered (ROT13)
# Next data row
# Should be added after progress is made on it’s own new line in the same file.
# Once you have traveled to the destination, walk into the palace and shout the passphrase(print the plain version) to the guard as you enter.
# After entering, locate the message (open file "{NextLocationId}_{PassPhrase}.gkg") and read the content.

# The “.gkg” file extension in this context means that the text file content is in ciphered form.
# It can be deciphered back to plain text using the Ceasar Cipher (ROT13).

# Read the first line as ciphered text and append it to the player_progress.txt.
# After the first line, save the plain version of the message into "{NextLocationId}-{PlainPassPhrase}.txt".

# Examples of message formats:

# file1: Ciphered message "{NextLocationId}_{PassPhrase}.gkg"
# file2: Plain version to save "{NextLocationId}-{PlainPassPhrase}.txt"

# After the progress and the Emperor’s message have been saved, the program closes with the final phrases.
# The next time the program runs, it should be able to read the previous progress from player_progress.txt and continue the next turn.

# Example program runs:

# Travel starting.
# Currently at home.
# Travelling to Galba's palace...
# ...Arriving to the Galba's palace.
# Passing the guard at the entrance.
# "Discipline!"
# Looking for the message in the palace...
# Ah, there it is! Seems cryptic.
# [Game] Progress autosaved!
# Deciphering Emperor's message...
# Looks like I've got now the plain version copy of the Emperor's message.
# Time to leave...
# Travel ending.

import os
from A6_T6 import rot13, writeFile
LOCATION_NAMES = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace"
}   
def readProgress(filename: str) -> tuple:
    """Reads the player progress from the specified file."""
    if not os.path.exists(filename):
        return (0, 1, "qvfpvcyvar")  # Default starting values

    with open(filename, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip()
        current_location, next_location, passphrase = last_line.split(';')
        return (int(current_location), int(next_location), passphrase)
def saveProgress(filename: str, current_location: int, next_location: int, passphrase: str):
    """Saves the player progress to the specified file."""
    with open(filename, 'a') as file:
        file.write(f"{current_location};{next_location};{passphrase}\n")
def readCipheredMessage(filename: str) -> str:
    """Reads the ciphered message from the specified file."""
    with open(filename, 'r') as file:
        return file.readline().strip()
def main():
    print("Travel starting.")
    
    progress_file = "player_progress.txt"
    current_location, next_location, passphrase = readProgress(progress_file)
    
    print(f"Currently at {LOCATION_NAMES[current_location]}.")
    print(f"Travelling to {LOCATION_NAMES[next_location]}...")
    print(f"...Arriving to the {LOCATION_NAMES[next_location]}.")
    print("Passing the guard at the entrance.")
    
    plain_passphrase = rot13(passphrase)
    print(f'"{plain_passphrase}"')
    
    print("Looking for the message in the palace...")
    ciphered_filename = f"{next_location}_{passphrase}.gkg"
    print("Ah, there it is! Seems cryptic.")
    
    print("[Game] Progress autosaved!")
    saveProgress(progress_file, next_location, next_location + 1, rot13(plain_passphrase))
    
    print("Deciphering Emperor's message...")
    ciphered_message = readCipheredMessage(ciphered_filename)
    plain_message = rot13(ciphered_message)
    
    plain_message_filename = f"{next_location}-{plain_passphrase}.txt"
    writeFile(plain_message_filename, plain_message)
    
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()