import art
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(text, type, shift):
    new_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if type == "encode":
                position += shift
            elif type == "decode":
                position -= shift

            if position >= len(alphabet):
                position = (position) - len(alphabet)
            new_text += alphabet[position]
        else:
            new_text += char
    print(f"The {type}d text is {new_text}")

print(art.logo)

isStop = False

while not isStop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, direction, shift)

    isDone = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if isDone == 'no':
        isStop = True
        print("Goodbye")