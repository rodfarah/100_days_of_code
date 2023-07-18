#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("/home/rofarah/Documents/TI/Code/100_days_of_code/mail_merge/Input/Names/invited_names.txt") as names_file:
    read_names = names_file.read()
    name_list = read_names.splitlines()

with open("mail_merge/Input/Letters/starting_letter.txt") as model:
    read_letter = model.read()

for name in name_list:
    with open(f"/home/rofarah/Documents/TI/Code/100_days_of_code/mail_merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as each_one:
        final_text = read_letter.replace("[name]", name)
        each_one.write(final_text)