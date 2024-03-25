import random


LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
SYMBOLS = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
]
NUMBERS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]


class PasswordGenerator:
    def __init__(self):
        self.password = ""

    def generate_password(self, nr_letters, nr_symbols, nr_numbers):
        characters = [LETTERS, SYMBOLS, NUMBERS]
        nr = [nr_letters, nr_symbols, nr_numbers]
        count = [1, 1, 1]

        for i in range(1, nr_letters + nr_numbers + nr_symbols + 1):
            character_type = random.randint(0, 2)

            while count[character_type] > nr[character_type]:
                character_type = random.randint(0, 2)

            count[character_type] += 1
            self.password += random.choice(characters[character_type])
        return self.password
