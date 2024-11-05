# U.S. States Game

This is an interactive game that helps users learn the U.S. states by guessing their names. Each correct guess displays the state's name on a map of the U.S., and if the user gives up, a list of missed states is saved to a file.

## 📋 Table of Contents
- [🎯 Objective](#-objective)
- [📂 Code Overview](#-code-overview)
- [⚙️ Requirements](#️-requirements)
- [▶️ How to Run](#️-how-to-run)
- [📄 License](#-license)

## 🎯 Objective
1. Display a blank map of the U.S. and prompt the user to guess the names of the states.
2. If a guess is correct, display the state name on the map.
3. When the user types "exit", save a list of states they missed to `states_to_learn.csv`.

## 📂 Code Overview

The following is the full code for `main.py`, which runs the game.

```python
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

    if answerState.lower() == "exit":
        missingStates = [state for state in allStates if state not in guessedStates]
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
```

### Explanation of the Code
1. Setup:
   - The map image is loaded and displayed using the Turtle Graphics library.
   - The list of states is read from 50_states.csv, which contains each state name and its coordinates on the map.
2. Game Loop:
   - While the user has not guessed all 50 states, the program prompts for the name of a state.
   - Correct Guess:
     - If the guessed state is correct, it is displayed at the correct coordinates.
   - Exit Option:
     - If the user types "exit", the game breaks out of the loop, saves a list of missed states to states_to_learn.csv, and exits.
3. Missed States:
   - All states that were not guessed are saved to states_to_learn.csv to help the user learn.

 ## ⚙️ Requirements
 - Python 3.x
 - turtle graphics library (included with Python)
 - pandas library (install using pip install pandas)
 - A file named blank_states_img.gif for the U.S. map image
 - A file named 50_states.csv containing:
   - state: Name of each U.S. state
   - x: x-coordinate on the map for the state name
   - y: y-coordinate on the map for the state name

## ▶️ How to Run
1. Ensure you have the following files:
  - main.py (this code file)
  - 50_states.csv (list of states with coordinates)
  - blank_states_img.gif (U.S. map image)
2. Run the program:
```bash
python main.py
```
3. Type in the names of U.S. states as you guess them. If you want to stop and see which states you missed, type "exit".
4. After exiting, check states_to_learn.csv for a list of states you missed.

## 📄 License
This project is open-source and available under the MIT License.


Enjoy learning the U.S. states with this interactive game! 🗺️

