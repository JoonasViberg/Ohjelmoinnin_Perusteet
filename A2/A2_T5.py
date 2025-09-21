# Make a Python program, which prompts for a compound word.

# Get following aspects from the word
#   Length
#   First character
#   Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Finally print the user specified substring.


# Program starting.
print("Program starting.", end="\n\n")
# Insert a closed compound word: Moonbanana
Word = input("Insert a closed compound word: ")

# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
Reversed = Word[::-1]
print(f"The word you inserted is '{Word}' and in reverse it is '{Reversed}'.")

# The inserted word length is 10
Length = len(Word)
print(f"The inserted word length is {Length}")

# Last character is 'a'
LastCharacter = Word[Length-1]
print(f"Last character is '{LastCharacter}'")

# Take substring from the inserted word by inserting...
print("\nTake substring from the inserted word by inserting...")

# 1) Starting point: 0
Start = int(input("1) Starting point: "))

# 2) Ending point: 4
End = int(input("2) Ending point: "))

# 3) Step size: 1
Step = int(input("3) Step size: "))

# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
Substring = Word[Start:End:Step]
print(f"\nThe word '{Word}' sliced to the defined substring is '{Substring}'.")

# Program ending.
print("Program ending.")