# Dia 4 - 100DaysOfCodeChallenge
# Banker Roulette
import random

name_list = input("Give me everybody's names, separeted by a comma.\n")
name_list = name_list.split(", ")
option = random.randint(0, len(name_list) - 1)
print(f"{name_list[option]} is going to buy the meal today!")

