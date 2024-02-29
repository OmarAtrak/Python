file = open("./input/letters/starting_letter.txt")
model = file.read()
file.close()

file = open("input/names/invited_names.txt")
names = file.read()
file.close()

names = names.split()


for name in names:
    name = name.strip()
    letter = model
    with open("./output/readyToSend/letter_for_" + name + ".txt", "w") as file:
        letter = letter.replace("[name]", f"{name}")
        file.write(letter)
