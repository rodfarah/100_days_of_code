from click import clear
from art import logo, vs
from random import randint
from game_data import data


def character_picker():
    """Return a character from data list and Delete character from list."""
    return data.pop(randint(0, len(data)-1))


class Opponent:
    """ Instantiate an opponent object"""

    def __init__(self, letter):
        character_data = character_picker()
        self.name = character_data.get("name")
        self.description = character_data.get("description")
        self.country = character_data.get("country")
        self.followers = character_data.get("follower_count")
        self.letter = letter


def winner(a_followers: int, b_folllowers: int) -> str:
    """Return the letter of the object who has more followers."""
    if a_followers > b_folllowers:
        return "A"
    return "B"


def lets_play():
    """Start Higher or Lower game."""
    first_round = True
    lose = False
    current_score = 0
    clear()
    print(logo)
    while len(data) > 0:
        if first_round:
            a = Opponent("A")
            b = Opponent("B")
        else:
            b = Opponent("B")

        print(
            f"Compare {a.letter}: {a.name}, a {a.description} from {a.country}. (f = {a.followers})")
        print(vs)
        print(
            f"Compare {b.letter}: {b.name}, a {b.description} from {b.country}. (f = {b.followers})")
        users_answer = input("Who has more followers? Type 'A' or 'B': ")
        right_answer = winner(a.followers, b.followers)
        if users_answer.upper() == right_answer:
            current_score += 1
            clear()
            print(logo)
            print(f"You are right! Current Score: {current_score}.")
            first_round = False
            if right_answer == "A":
                a = b
                a.letter = "A"
            else:
                del b
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            exit()
    return "Congratulations! You've just reached the maximum score!"


print(lets_play())
