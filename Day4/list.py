names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")


name_lenght = len(names)

import random
random_index = random.randint(0, name_lenght - 1)
print(names[random_index])
