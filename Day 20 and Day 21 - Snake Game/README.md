## Steps to build the Snake Game
1. Creating `main.py` with the essentials
2. Create a snake body
3. Move the snake
4. Create snake food
5. Detect Collision with food
6. Create scoreboard
7. Detect collision with wall
8. Detect collision with tail

## Creating `main.py` with the essentials
```py
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


screen.exitonclick()
```

## Create a snake body
For creating a rectangle, we use 3 different squares stacked along each other. To achieve this we use a for loop to construct the turtles
```py
starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
	new_segment = Turtle("square")  
    new_segment.color("white")  
    new_segment.goto(position)
    segments.append(new_segment)  
screen.exitonclick()
```

## Move the snake
