import hashlib
from typing import List, Optional

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    encoded_password = password.encode('utf-8')
    hasher = hashlib.md5(encoded_password)
    return hasher.hexdigest()

def _get_credentials_list() -> List[List[str]]:
    """Helper to read all credentials into a list of lists."""
    credentials_list = []
    try:
        with open(CREDENTIALS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    credentials_list.append(line.split(DELIMITER))
    except FileNotFoundError:
        pass
    return credentials_list

def _write_credentials_list(credentials_list: List[List[str]]) -> None:
    """Helper to write a list of credentials back to the file."""
    with open(CREDENTIALS_FILE, 'w') as file:
        for user_data in credentials_list:
            file.write(DELIMITER.join(user_data) + '\n')

def register(PUsername: str, PPassword: str) -> bool:
    """
    Register a new user by appending their credentials to the file.
    Returns True if registration succeeds (username is new), False otherwise.
    """
    credentials_list = _get_credentials_list()
    
    # Check for existing username (not strictly required, but good practice)
    for user_data in credentials_list:
        if user_data[1] == PUsername:
            return False

    # Count existing users to assign a new ID (ID is the first column)
    new_id = len(credentials_list)
    
    # Hash the password
    password_hash = hash_password(PPassword)
    
    # New user data: [ID, Username, Hashed Password]
    new_user_data = [str(new_id), PUsername, password_hash]
    
    # Write the new user data to the file
    with open(CREDENTIALS_FILE, 'a') as file:
        file.write(DELIMITER.join(new_user_data) + '\n')
    
    return True


def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    input_hash = hash_password(PPassword)
    
    credentials_list = _get_credentials_list()
    
    for user_data in credentials_list:
        username, stored_hash = user_data[1], user_data[2]
        
        if username == PUsername and stored_hash == input_hash:
            return True
            
    return False


def viewProfile(PUsername: str) -> List[str]:
    """
    Return the user ID and username for the given username.
    Returns [ID, Username] or an empty list if not found.
    """
    credentials_list = _get_credentials_list()
    
    for user_data in credentials_list:
        if user_data[1] == PUsername:
            # Return [ID, Username]
            return [user_data[0], user_data[1]] 
            
    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    credentials_list = _get_credentials_list()
    
    updated_hash = hash_password(PNewPassword)
    found = False
    
    for i, user_data in enumerate(credentials_list):
        if user_data[1] == PUsername:
            # Index 2 is the password hash
            credentials_list[i][2] = updated_hash 
            found = True
            break

    if found:
        _write_credentials_list(credentials_list)