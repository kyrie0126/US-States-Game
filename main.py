import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# read in data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

FONT = ("Courier", 10, "normal")

guessed_states = []

alive = True
while alive:
    score = len(guessed_states)
    guess = screen.textinput(title=f"Guessed states: {score}/50", prompt="What's your guess?").title()

    if guess in all_states and guess not in guessed_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        state_info = data[data.state == guess]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(state_info.state.item(), align="center", font=FONT)
        screen.update()

    else:
        t.goto(0,0)
        t.write("Game Over", align="center", font=("Courier", 30, "bold"))
        to_learn = [state for state in all_states if state not in guessed_states]
        df_learn = pd.DataFrame(to_learn, columns=["States to Learn"])
        df_csv = df_learn.to_csv("states_to_learn.csv")

        alive = False


screen.exitonclick()