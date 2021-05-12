# Dia 8 - 100DaysOfCodeChallenge
# Caesar Cipher
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_word = []
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if position+shift > 25:
                new_position = new_position - 26
            new_word.append(alphabet[new_position])
        else:
            new_word.append(letter)
    new_word = "".join(new_word)
    print(f"The text {direction}d is {new_word}")

print(art.logo)
go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
    else:
        print("Invalid option")
    option = input("\nType 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if option == "no":
        go_again = False

