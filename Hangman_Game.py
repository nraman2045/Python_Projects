import random
import hangman_words
import hangman_art
# from replit import clear

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')  # just for example

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # clear()

    if guess in display:
        print(f"You have already entered {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        while guess not in chosen_word:
            print(f"The letter {guess} is not in the word , You lose a life")
            break
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])