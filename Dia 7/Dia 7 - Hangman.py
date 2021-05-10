# Dia 7 - 100DaysOfCodeChallenge
# Hangman
import random
from hangman_words import word_list
import hangman_art as h
import os

end_of_game = False
lives = 6

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print(h.logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# List with underscores
display = []
for _ in chosen_word:
    display += "_"
print(h.stages[6])
print(f"The word is similar to: {display}")
already_guessed = []
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

    guess = (input("Guess a letter: ")).lower()
    os.system('cls') 
    if guess not in already_guessed:
        already_guessed += guess
    else:
        guess = (input(f'You already guessed "{guess}". Guess a different one: ')).lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in chosen_word:
        for index in range(word_length):
            if guess == chosen_word[index]:
                display[index] = guess
    else: 
        print(f'\n\nThe letter "{guess}" is wrong')
        lives -= 1
    print(h.stages[lives])
    if (lives == 0):
        print("\nYou lose")
        end_of_game = True
        print(f"The word was: {chosen_word}")
    if "_" not in display:
        print("\nYou win")
        end_of_game = True
    print(f"{' '.join(display)}")
