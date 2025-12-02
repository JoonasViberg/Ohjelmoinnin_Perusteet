# Build “rock-paper-scissors” game in Python. In this game, there are two players, user and bot named “RPS-3PO”.

# Rules for the RPS game:

# Rock beats scissors
# Paper beats rock
# Scissors beat paper
# ASCII Art below for the game.

#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)

#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)

#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# In this exercise, place the following at the beginning of the code (right at the top).
# Setting the seed value means we are setting an initial state for the random number generator. After this, the generated numbers will follow exactly the same sequence. 
# he random number will then depend on the number of calls to the random function.

# import random
# random.seed(1234)
# Randomize the bot’s choice in each game by calling the random.randint(1, 3) function with the given arguments.
# This function call returns a random integer between 1 and 3, inclusive. Implementing randomness in another way may lead to varying test results and is therefore not recommended.

# The program start by asking for the player’s name. Then, greet the player and announce the opponent. After that, inform that the game is starting.

# The menu contains 4 options, first three are game related options. If user chooses rock, paper or scissors from the menu, a round will be played.

# Display text "Rock! Paper! Scissors! Shoot!\n". Then, reveal the player’s choice first, followed by the bot’s choice.
# Show a decorative line of 25 hash (#) symbols between and around the choices to visually separate the player’s and the bot’s selections.

# Then check the players’ choice according to the rules of the RPS game. If both players have chosen the same option, the result is a draw ("Draw! Both players chose ____.").
# Otherwise, declare the winner and the reason for the victory based on the condition.

# Example program runs

# Program starting.
# Welcome to the rock-paper-scissors game!
# Insert player name: John
# Welcome John!
# Your opponent is RPS-3PO.
# Game starts...

# Options:
# 1 - Rock
# 2 - Paper
# 3 - Scissors
# 0 - Quit game
# Your choice: 1
# Rock! Paper! Scissors! Shoot!

# #########################
# John chose rock.

#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)

# #########################
# RPS-3PO chose paper.

#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)

# #########################

# RPS-3PO paper beats John rock.

# Options:
# 1 - Rock
# 2 - Paper
# 3 - Scissors
# 0 - Quit game
# Your choice: 0

# Results:
# John - wins (0), losses (1), draws (0)
# RPS-3PO - wins (1), losses (0), draws (0)

# Program ending.

# Example solution contains 162 lines of code.

import random

def main() -> None:
    random.seed(1234)
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    ascii_art = {
        "rock": """    _______
---'  ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
        "paper": """      _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""",
        "scissors": """    _______
---'  ____)____
           ______)
          __________)
        (____)
---.__(___)"""
    }
    player_wins = 0
    player_losses = 0
    draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        
        try:
            player_choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 3.")
            continue
        
        if player_choice == 0:
            break
        if player_choice not in choices:
            print("Invalid choice. Please select a valid option.")
            continue
        
        bot_choice = random.randint(1, 3)
        
        print("Rock! Paper! Scissors! Shoot!\n")
        
        print("#" * 25)
        print(f"{player_name} chose {choices[player_choice]}.\n")
        print(ascii_art[choices[player_choice]])
        print("\n" + "#" * 25)
        print(f"RPS-3PO chose {choices[bot_choice]}.\n")
        print(ascii_art[choices[bot_choice]])
        print("\n" + "#" * 25 + "\n")
        
        if player_choice == bot_choice:
            draws += 1
            print(f"Draw! Both players chose {choices[player_choice]}.\n")
        elif (player_choice == 1 and bot_choice == 3) or \
             (player_choice == 2 and bot_choice == 1) or \
             (player_choice == 3 and bot_choice == 2):
            player_wins += 1
            print(f"{player_name} {choices[player_choice]} beats RPS-3PO {choices[bot_choice]}.\n")
        else:
            player_losses += 1
            print(f"RPS-3PO {choices[bot_choice]} beats {player_name} {choices[player_choice]}.\n")

    print("Results:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({draws})")
    print(f"RPS-3PO - wins ({player_losses}), losses ({player_wins}), draws ({draws})")
    print("Program ending.")
    
if __name__ == "__main__":
    main()