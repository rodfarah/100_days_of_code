from random import randint
from art import logo

print(logo)
print("Welcome to the Guess the Number game!\nI am thinking of a number between 1 and 100.")

attempts_dict = {"easy": 10, "hard": 5}
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
num_of_attempts = attempts_dict[difficulty.lower()]

base_number = randint(1, 100)

while num_of_attempts > 0:
    print(
        f"You have {num_of_attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == base_number:
        print(f"Right answer! I have chosen number {base_number}!")
        break
    elif guess > base_number:
        print("Too high.")
        num_of_attempts -= 1
        if num_of_attempts >= 1:
            print("Guess again.")
        else:
            print("You lose!")
            break
    else:
        print("Too low.")
        num_of_attempts -= 1
        if num_of_attempts >= 1:
            print("Guess again.")
        else:
            print("You lose!")
            break
