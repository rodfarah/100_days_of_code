##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
from random import randint


# Datetime definitions:
now = dt.datetime.now()
today_day_month = (now.day, now.month)

# Getting the data:
data = pd.read_csv("birthday_wisher/birthdays.csv")
df = pd.DataFrame(data)

data_dict = {(day, month) : [name, email] for name, email, day, month in zip(df["name"], df["email"], df["day"], df["month"])}


for tpl in data_dict.keys():
    if tpl == today_day_month:
        name = data_dict[tpl][0]
        email_adress = data_dict[tpl][1]
        print(f"Today is {name}'s birthday and his/her email adress is {email_adress}!\nHere is the letter:\n\n")
        with open(f"birthday_wisher/letter_templates/letter_{randint(1,3)}.txt") as birthday_letter:
            content = birthday_letter.read()
            proper_name_letter = content.replace("[NAME]", name)
        print(proper_name_letter)
    print("No birthday today!")