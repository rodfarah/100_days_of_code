import random

from click import clear
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

current_word = random.choice(word_list)
underline_list = ["_" for _ in range(len(current_word))]
lives = 6
past_guesses = []

while "_" in underline_list:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in past_guesses:
        print(f"You have already picked letter '{guess}'.")
        print(stages[lives])
        continue
    else:
        past_guesses.append(guess)

    if guess not in current_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(" ".join(underline_list))
            print(stages[lives])
            break
        print(" ".join(underline_list))
        print(stages[lives])
        continue
    else:
        idx = 0
        for letter in current_word:
            if letter == guess:
                underline_list[idx] = letter
                idx += 1
            else:
                idx += 1
        print(" ".join(underline_list))
        if "_" not in underline_list:
            print("You win.")
            print(stages[lives])
            break
        print(stages[lives])
