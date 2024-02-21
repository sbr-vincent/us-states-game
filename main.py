import turtle
import pandas

FONT = ("Courier", 8, "normal")

screen = turtle.Screen()

screen.title("U.S. States Game")
# Path to my image
image = "blank_states_img.gif"
# Create a shape using the US image. Only takes gif files
screen.addshape(image)
# Make a turtle of that new shape
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct_states = []

while len(correct_states) < 50:
    answer_state = (screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                     prompt="What's another state's name?")).title()
    if answer_state == "Exit":
        missed_states = []
        for s in state_list:
            if s not in correct_states:
                missed_states.append(s)

        missed_dict = {"State": missed_states}

        df = pandas.DataFrame(missed_dict)
        df.to_csv("learn.csv")
        break

    if answer_state in state_list:
        if answer_state not in correct_states:
            correct_states.append(answer_state)
            state = data[data["state"] == f"{answer_state}"]
            input_state = turtle.Turtle()
            input_state.hideturtle()
            input_state.penup()
            input_state.speed("fastest")
            input_state.goto(int(state['x']), int(state["y"]))
            input_state.write(f"{answer_state}", font=FONT)


# Used to get the coordinates of the states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# # The same as screen.exitonclick to keep the screen up but it won't close the screen when we click
# turtle.mainloop()

# Create a csv of the states that were missed called learn.csv

screen.exitonclick()