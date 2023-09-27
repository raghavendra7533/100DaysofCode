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
To move the snake, I created another `.py` file where I started coding the characteristics of the snake. In the snake file I declared the construction of the snake and movement of the snake.
- I declared a constant called `STARTING_POSITIONS` and set it to the cords.
- I declared another constant called `MOVE_DISTANCE` and set it to the speed of the snake

```py
#snake.py
from turtle import Turtle  
  
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]  
MOVE_DISTANCE = 20  
class Snake:  
    def __init__(self):  
        self.segments = []  
        self.create_snake()  
  
  
    def create_snake(self):  
        for position in STARTING_POSITIONS:  
            new_segment = Turtle("square")  
            new_segment.color("white")  
            new_segment.penup()  
            new_segment.goto(position)  
            self.segments.append(new_segment)  
  
    def move(self):  
        for seg_num in range(len(self.segments) - 1, 0, -1):  
            new_x = self.segments[seg_num - 1].xcor()  
            new_y = self.segments[seg_num - 1].ycor()  
            self.segments[seg_num].goto(new_x, new_y)  
        self.segments[0].forward(MOVE_DISTANCE)
```

```py
#main.py
from turtle import Turtle, Screen  
import time  
from snake import Snake  
  
screen = Screen()  
screen.setup(width=600, height=600)  
screen.bgcolor("black")  
screen.title("Snake Game")  
screen.tracer(0)  
  
snake = Snake()  
  
game_is_on = True  
while game_is_on:  
    screen.update()  
    time.sleep(0.1)  
    snake.move()
```
