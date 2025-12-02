# Create program which can handle basic user registrations and logins.
# For this exercise, study the built-in library hashlib.
# The passwords must be hashed with md5 and hexdigested to a string format.
# It isn’t necessary to implement unique constraints on usernames.

# Main menu options:

# Login
# Register
# Exit
# User menu options:

# View profile
# Change passsword (no need to implement)
# Logout
# Use “credetials.txt” filename as place to store the credentials in CSV format.
# The filename can be defined as constant variable on the top-level of the library file.
# The value separator or delimiter must be a semicolon “;”.

# Example “credentials.txt”:

# 0;admin;58d613129c5e71de57ee3f44c5ce16bc

# Example program runs:

# Program starting.
# Options:
# 1 - Login
# 2 - Register
# 0 - Exit
# Your choice: 2
# Insert username: John
# Insert password: SecretPassword
# User registration completed!

# Options:
# 1 - Login
# 2 - Register
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.

from loginLib import login, register, viewProfile, change_password
from typing import Optional

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    logged_in_user: Optional[str] = None
    while True:
        if logged_in_user:
            logged_in_user = userMenu(logged_in_user)
            continue
            
        showOptions()
        try:
            choice = askChoice()
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1: # Login
            username = askValue("username")
            password = askValue("password")
            
            if login(username, password):
                print(f"Login successful. Welcome, {username}!")
                logged_in_user = username
            else:
                print("Login failed. Invalid username or password.")
            
        elif choice == 2: # Register
            username = askValue("username")
            password = askValue("password")
            
            if register(username, password):
                print("User registration completed!")
            else:
                print("Registration failed. Username may already exist.")
            
        elif choice == 0: # Exit
            break
            
        else:
            print("Invalid choice.")


def userMenu(PUsername: str) -> Optional[str]:
    """Handles user-specific actions. Returns PUsername if staying logged in, else None."""
    while True:
        showUserMenu()
        try:
            choice = askChoice()
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1: # View profile
            profile = viewProfile(PUsername)
            if profile:
                # profile format: [ID, Username]
                print("\n--- User Profile ---")
                print(f"ID: {profile[0]}")
                print(f"Username: {profile[1]}")
                print("--------------------")
            else:
                print("Error: Could not retrieve profile.")
            
        elif choice == 2: # Change password
            print("Password change is not implemented in this version.")
            # For demonstration, you could implement a prompt here:
            # new_password = askValue("new password")
            # change_password(PUsername, new_password)
            # print("Password updated!")
            
        elif choice == 0: # Logout
            print(f"User {PUsername} logged out.")
            return None # Signal logout to mainMenu loop
            
        else:
            print("Invalid choice.")
            
        # If the user performed an action other than Logout, stay in the loop (return PUsername)
        # Note: We only return None on logout (choice 0)

def askChoice() -> int:
    """Prompts for and returns an integer choice."""
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    """Prompts for and returns a string value."""
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()