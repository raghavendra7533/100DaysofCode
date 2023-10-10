import turtle
import pandas

"""Constants"""
CSV_FILE = "50_states.csv"
FONT = ("Courier", 10, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")


screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(CSV_FILE)
all_states = data.state.to_list()
print(all_states)
guessed_state = []
number_guessed = 0
is_game_on = True

while len(guessed_state) < 50 and is_game_on:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What's another states name?")
    answer_state = answer_state.title()
    print(answer_state)

    if answer_state in all_states:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            x = int(state_data.x)
            y = int(state_data.y)
            t.goto(x, y)
            t.write(f"{answer_state}", font=FONT)
        elif answer_state == "exit":
            break
        else:
            continue
    else:
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(0,0)
        game_over.write("Game Over", font=GAME_OVER_FONT, align="center")
        is_game_on = False


screen.exitonclick()
