# Dia 4 - 100DaysOfCodeChallenge
# Rock, paper or scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

l = [rock, paper, scissors]
user_option = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(l[user_option])
print("Computer chose:")
computer_option = random.randint(0,2)
print(l[computer_option])

if(user_option == computer_option):
    print("It's a draw")
elif(user_option == 1 and computer_option == 0):
    print("You win!")
elif(user_option == 1 and computer_option == 2):
    print("You lose...")
elif(user_option == 0 and computer_option == 1):
    print("You lose...")
elif(user_option == 0 and computer_option == 2):
    print("You win!")
elif(user_option == 2 and computer_option == 0):
    print("You lose...")
elif(user_option == 2 and computer_option == 1):
    print("You win!")