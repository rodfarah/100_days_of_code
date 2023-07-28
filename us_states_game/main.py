import turtle
import pandas as pd
import filling_states as fs

# screen set:
screen = turtle.Screen()
screen.setup(width=740, height=510)
screen.title("U.S. States Game")
map_image = "us_states_game/blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)


# data set:
all_states = pd.read_csv("us_states_game/50_states.csv")
states_list = all_states["state"].to_list()
wright_answer_list = []
missing_states_list = []


def state_coord(state: str) -> tuple:
    """Return (x, y) coordinates of a given U.S State"""
    state_row = all_states[all_states["state"] == state]
    return (state_row["x"].item(), state_row["y"].item())


def message_board(title: str,  specific_msg: str, general_msg: str):
    """
    Pop up a message window and ask user to type 'OK'.
        title (str): Do not insert a period in the end.
        specific_msg (str): In the end, insert colon (if needed), but not a space.
        general_msg (str): Do not insert a period in the end.
    """
    while True:
        alert = screen.textinput(
            title.upper(), f"{specific_msg} {general_msg}. Type OK!")
        if alert.upper() == "OK":
            break


def missing_states(correct: list[str]) -> dict[str]:
    """Generate a dictionary of missing U.S States, given a list of already found ones."""
    for state in states_list:
        if state not in wright_answer_list:
            missing_states_list.append(state)
    return {"Missing States": missing_states_list}


while len(wright_answer_list) < 50:
    chosen_state = screen.textinput(
        f"{len(wright_answer_list)}/50 States Correct", "Insert a State Name:").title()
    if chosen_state == "Exit":
        message_board(title="exit", specific_msg="You quit:",
                      general_msg="A CSV file containing all missing States wil be generated")
        data_frame = pd.DataFrame(missing_states(wright_answer_list))
        data_frame.to_csv("us_states_game/missing_states.csv")
        break
    elif chosen_state in wright_answer_list:
        message_board(title="ALREADY PICKED",
                      specific_msg=f"{chosen_state}: ", general_msg="You have already chosen this before")
        continue
    elif chosen_state in states_list:
        wright_answer_list.append(chosen_state)
        correct_state = fs.StateFill(chosen_state, state_coord(chosen_state))
    else:
        message_board(title="NOT A STATE",
                      specific_msg=f"{chosen_state}", general_msg="is not an U.S State")
        continue

if len(wright_answer_list) == 50:
    message_board("Congratulations!", "Very clever!",
                  "You have found all 50 U.S. States!")
