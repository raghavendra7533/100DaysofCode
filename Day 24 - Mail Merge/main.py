PLACEHOLDER = '[name]'


with open("./Input/Names/invited_names.txt") as input_file:
    names = input_file.readlines()

list_names = []
for name in names:
    list_names.append(name.strip())

with open("./Input/Letters/starting_letter.txt") as input_letter:
    letter = input_letter.read()
    letter = letter.strip()
    for name in list_names:
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as output_file:
            output_file.write(new_letter)
