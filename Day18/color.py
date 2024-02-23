import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def choice_color(colors_list):
    selected_color = random.choice(colors_list)
    return selected_color
