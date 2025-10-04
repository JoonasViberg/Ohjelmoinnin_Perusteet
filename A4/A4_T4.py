# Make a program, which prompts user to insert words.
# Program must stop prompting words if user inserts empty word.
# After stopping the repetitive prompt, print the amount of words and characters that the user inserted



# Program starting.
print("Program starting.\n")

# Insert word (empty stops): Close
word_count = 0
char_count = 0
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    word_count += 1
    char_count += len(word)
# Insert word (empty stops): the
# Insert word (empty stops): loop
# Insert word (empty stops): 
#
# You inserted:
print(f"\nYou inserted:\n- {word_count} words\n- {char_count} characters")
# - 3 words
# - 12 characters
#
# Program ending.
print("\nProgram ending.")