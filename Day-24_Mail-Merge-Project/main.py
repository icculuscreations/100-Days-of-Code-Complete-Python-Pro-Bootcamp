PLACEHOLDER = "[name]"


with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()
with open("Input/Letters/starting_letter.txt") as starting_letter:
    starting_letter_text = starting_letter.read()
for name in names:
    new_letter_text = starting_letter_text.replace(PLACEHOLDER, name)
    with open(f"Output/ReadyToSend/letter_for_{name}", "w") as new_letter:
        new_letter.write(new_letter_text)
