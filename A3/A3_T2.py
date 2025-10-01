# Make Python program which does the following steps:

# Prompt user to insert
# A word
# A character
# Find if the character exists in the word. Possible prints below.
# Word "{WordFirst}" contains character "{Character}"
# Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# Both inserted words are the same alphabetically, "{WordFirst}"



# Program starting.
print("Program starting.")

# String comparisons
print("String comparisons.")

# Insert first word: beans
word1 = input("Insert first word: ")

# Insert a character: n
char = input("Insert a character: ")

# Word "beans" contains character "n"
if char in word1:
    print(f'Word "{word1}" contains character "{char}".')
else:
    print(f'Word "{word1}" doesn\'t contain character "{char}".')

# Insert second word: banana
word2 = input("Insert second word: ")

# The second word "banana" is before the first word "beans" alphabetically.
if word1 < word2:
    print(f'The first word "{word1}" is before the second word "{word2}" alphabetically.')
elif word2 < word1:
    print(f'The second word "{word2}" is before the first word "{word1}" alphabetically.')
elif word1 == word2:
    print(f'Both inserted words are the same alphabetically, "{word1}".')
else:
    print("Unknown error.")
# Program ending.
print("Program ending.")