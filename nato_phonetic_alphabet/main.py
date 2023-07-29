# # My first solution: unfortunately I did not use pandas  :-(

# with open("nato_phonetic_alphabet/nato_phonetic_alphabet.csv") as all_data:
#     full_data = all_data.read()
# print(full_data)

# first_step = full_data.splitlines()
# print("\n", first_step)

# spell_list = [string.split(",") for string in first_step]
# print("\n", spell_list)

# spell_dict = {letter:code for letter, code in spell_list[1:]}
# print("\n", spell_dict)

# def spell_word(word: str) -> list[str]:
#     """Spell a given word using Nato Phonetic Alphabet"""
#     return [spell_dict[letter.upper()] for letter in word]


# print(spell_word("Rodrigo"))

# Second solution (now using pandas as teacher suggests)

import pandas as pd

all_data = pd.read_csv("nato_phonetic_alphabet/nato_phonetic_alphabet.csv")
print(all_data)

spell_dict = {row.letter:row.code for idx, row in all_data.iterrows()}
print(spell_dict)

word = input("Give me a word and I will spell it using NPA: ").upper()
print([spell_dict[letter] for letter in word])