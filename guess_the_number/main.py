from random import randint
from art import logo

print(logo)
print("Welcome to the Guess the Number game!\nI am thinking of a number between 1 and 100.")
BASE_NUMBER = randint(1, 100)
print(BASE_NUMBER)


def initial_attempts():
    """Return number of attempts based on the player's difficulty choice."""
    attempts_dict = {"easy": 10, "hard": 5}
    easy_or_hard = input("Chose a difficulty. Type 'easy' or 'hard': ")
    return attempts_dict[easy_or_hard.lower()]


def guess_checker(guess: int, number: int, attempts: int) -> int:
    """ Decrease number of attempts if guess is wrong. Message and exit the program otherwise."""
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The secret number is {number}")
        return 0
        exit()


def lets_play():
    """ Play 'Guess the Number' game"""
    num_of_attempts = initial_attempts()

    while num_of_attempts > 0:
        print(f"You have {num_of_attempts} attempts.")
        guess = int(input("Make a guess: "))
        num_of_attempts = guess_checker(guess, BASE_NUMBER, num_of_attempts)
    return "No more attempts left. You lose!"


print(lets_play())
