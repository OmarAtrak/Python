import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)


data = pandas.read_csv("data/50_states.csv")
all_states = data["state"].to_list()

state_correct_count = 0
guessed_states = []


while len(guessed_states) < len(all_states):
    state = screen.textinput(title="What's another state's name?", prompt="Guess a state").title()
    if state in all_states:
        guessed_states.append(state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == state]
        turtle.goto(int(state_data["x"]), int(state_data["y"]))
        turtle.write(state_data.state.item())
        state_correct_count += 1


screen.mainloop()
