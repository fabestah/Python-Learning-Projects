import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Naming Game")
bckgr = "blank_states_img.gif"
game_is_on = True

screen.addshape(bckgr)

turtle.shape(bckgr)

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
already_guessed = []

while len(already_guessed) < 50:  
    answer_state = screen.textinput(
        title=f"{len(already_guessed)}/50 States", prompt="What's another state's name?"
    )
    answer = answer_state

    

    for s in states:
        if answer.lower() == s.lower():
            if answer.lower() not in already_guessed:
                already_guessed.append(answer.lower())
                state = data[data.state == s]
                x = int(state["x"])
                y = int(state["y"])
                new_t = turtle.Turtle()
                new_t.speed("fastest")
                new_t.ht()
                new_t.penup()
                new_t.goto(x, y)
                new_t.write(answer.capitalize(), False, align="center")

    if answer.lower() == "exit":
        not_guessed = [x for x in states if x.lower() not in already_guessed]
        not_guessed_data = pandas.DataFrame(not_guessed)
        not_guessed_data.to_csv("states_not_guessed.csv")
        break

turtle.mainloop()
