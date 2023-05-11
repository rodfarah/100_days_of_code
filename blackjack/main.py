from click import clear
from blackjack_art import logo
import random


def card_picker():
    """Return the value of a random card picked from a pack of cards."""
    return random.choice([[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])


def ace_or_others(score, card):
    if type(card) is list and score > 10:
        return card[0]
    elif type(card) is list:
        return card[1]
    else:
        return card


def compare_results(human: int, computer: int) -> str:
    """Return the game winner."""
    if human > 21:
        return "You went over. You lose 😭"
    elif computer > 21:
        return "Opponent went over. You win 😁"
    elif human == computer:
        return "Draw 🙃"
    elif computer == 21:
        return "Lose, opponent has Blackjack 😱"
    elif human == 21:
        return "Win with a Blackjack 😎"
    elif human < computer:
        return "You lose 😤"
    else:
        return "You win 😃"


def lets_play():
    print(logo)
    # Computer:
    computer_cards = []
    computer_current_score = 0
    while computer_current_score < 17:
        computer_cards.append(ace_or_others(
            computer_current_score, card_picker()))
        computer_current_score = sum(computer_cards)

    # Human:
    human_cards = []
    human_current_score = 0
    for _ in range(2):
        human_cards.append(ace_or_others(human_current_score, card_picker()))
        human_current_score = sum(human_cards)
    print(f"Your cards: {human_cards}, current score: {human_current_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    another_one = input("Type 'y' to get another card, type 'n' to pass: ")
    while another_one == "y":
        human_cards.append(ace_or_others(human_current_score, card_picker()))
        human_current_score = sum(human_cards)
        print(
            f"Your cards: {human_cards}, current score: {human_current_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if human_current_score > 21:
            break
        else:
            another_one = input(
                "Type 'y' to get another card, type 'n' to pass: ")
    print(
        f"Your final hand: {human_cards}, final score: {human_current_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_current_score}")
    print(compare_results(human_current_score, computer_current_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    lets_play()
