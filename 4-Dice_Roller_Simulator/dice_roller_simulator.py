import os
import random

def roll_dice():
    return random.randint(1, 6)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    choice = input("Press exit to quit or press any key to roll the dice: ").strip().lower()
    if choice in ['exit', 'quit', 'q', 'e']:
        break
    else:
        clear_screen()
        print(f"You rolled a {roll_dice()}!")