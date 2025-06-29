import random
import string
import os

# Character sets
UPPER_CASE = string.ascii_uppercase
LOWER_CASE = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL_CHARS = string.punctuation

# Default settings
password_length = 4
password_types = UPPER_CASE + LOWER_CASE  # Default to upper and lower

def generate_password(length: int, types: str) -> str:
    """Generate a random password of the given length and character types."""
    if not types:
        raise ValueError("No character types selected for password.")
    return ''.join(random.choice(types) for _ in range(length))

def settings() -> None:
    """Set the password length and character types."""
    global password_length, password_types

    # Set password length
    try:
        pass_len_command = input("Enter the length of the password: ")
        password_length = int(pass_len_command)
    except ValueError:
        print("Invalid input. Using previous length:", password_length)

    # Set password character types
    print(
        "\nEnter the character types to include (any combination):\n"
        "  ▶ a = All types\n"
        "  ▶ u = Uppercase letters\n"
        "  ▶ l = Lowercase letters\n"
        "  ▶ n = Numbers\n"
        "  ▶ s = Special characters\n"
        "Example: 'uln' for uppercase, lowercase, and numbers"
    )

    pass_types_command = input("Your choice: ").lower()
    types = ""

    if "a" in pass_types_command:
        types = UPPER_CASE + LOWER_CASE + NUMBERS + SPECIAL_CHARS
    else:
        if "u" in pass_types_command:
            types += UPPER_CASE
        if "l" in pass_types_command:
            types += LOWER_CASE
        if "n" in pass_types_command:
            types += NUMBERS
        if "s" in pass_types_command:
            types += SPECIAL_CHARS

    if not types:
        print("No valid character types selected. Using default (uppercase + lowercase).")
        types = UPPER_CASE + LOWER_CASE

    password_types = types

def clear_screen():
    """Clear the screen (cross-platform)"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Main loop
while True:
    print("\nWelcome to the Password Generator!")
    print("1. Generate a password")
    print("2. Settings")
    print("3. Clear the screen")
    print("4. Quit")

    choice = input("Enter your choice: ").strip()

    if choice in ["4", "quit", "exit"]:
        print("Goodbye!")
        break
    elif choice == "1":
        password = generate_password(password_length, password_types)
        print(f"Generated Password: {password}")
    elif choice == "2":
        settings()
    elif choice in ["3", "clear", "cls"]:
        clear_screen()
    else:
        print("Invalid choice. Please try")