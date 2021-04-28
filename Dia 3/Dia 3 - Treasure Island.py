# Dia 3 - 100DaysOfCodeChallenge
# Treasure Island
from colorama import Fore, Style

print("Welcome to Treasure Island. Your mission is to find the treasure\n")
c1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if c1 == "left":
    c2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if c2 == "wait":
        c3 = input(f"You arrive at the island unharmed. There is a house with 3 doors. One {Fore.RED}red{Style.RESET_ALL}, one {Fore.YELLOW}yellow{Style.RESET_ALL}" +  
        f"and one {Fore.BLUE}blue{Style.RESET_ALL}. Which colour do you choose? \n").lower()
        if c3 == "red":
            print("It's a room full of fire. Game Over.")
        elif c3 == "yellow":
            print("You found the treasure! You Win!")
        elif c3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
