import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
allStates = data.state.to_list()

guessedStates = []

while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States Correct", prompt="What's another state's name?").title()

    # If answerState is one of the states in all the states of the 50_states.csv
    #   If they got it right :
    #       Create a turtle to write the name of the state at the state's x and y coordinates
    if answerState.lower() == "exit":
        missingStates = []
        for state in allStates:
            if state not in guessedStates:
                missingStates.append(state)
        newData = pandas.DataFrame(missingStates)
        newData.to_csv("states_to_learn.csv")
        break
    if answerState in allStates:
        guessedStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.state == answerState]
        t.goto(stateData.x.item(), stateData.y.item())
        t.write(answerState)


