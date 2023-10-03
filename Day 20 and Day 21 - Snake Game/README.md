## Steps to build the Snake Game
1. Creating `main.py` with the essentials
2. Create a snake body
3. Move the snake
4. Create snake food
5. Detect Collision with food
6. Create scoreboard
7. Detect collision with wall
8. Detect collision with tail
9. Full Code

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

and the main file was
```py
from turtle import Turtle, Screen  
import time  
from snake import Snake  
  
screen = Screen()  
screen.setup(width=600, height=600)  
screen.bgcolor("black")  
screen.title("Snake Game")  
screen.tracer(0)  
  
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
  
game_is_on = True  
while game_is_on:  
    screen.update()  
    time.sleep(0.1)  
    snake.move()
```

## Class Inheritance
In order to inherit the characteristics of another class, we must specify the class we are inheriting from within a pair of parenthesis during the initialisation.
#### Syntax
```py
class Fish(Animal): #here 'Animal' is the class we are inheriting from
	def __init__(self):
		super().__init__() # here we are initialising all the characteristics of the super class, in this case, all the characteristics of the 'Animal' class.
```

#### Example code
```py
class Animal:
	def __init__(self):
		self.num_eyes = 2
	def breathe(self):
		print("Inhale, Exhale")

class Fish(Animal):
	def __init__(self):
		super().__init__()
	def breathe(self):	
		super().breathe()
		print("Doing this underwater.")
	def swim(self):
		print("moving in water.")

nemo = Fish()
nemo.swim() # output: "moving in water"
nemo.breathe() # output: "Inhale, Exhale \n Doing this underwater."
print(nemo.num_eyes) # output: "2"
```

## Creating `Scoreboard.py` to keep score
The scoreboard is also a Turtle, first importing Turtle from the library, and declaring the constants like fonts and alignment.
```py
from turtle import Turtle  
  
  
ALIGNMENT = "center"  
FONT = ("Courier", 24, "normal")  
  
class Scoreboard(Turtle):  
    def __init__(self):  
        super().__init__()  
        self.score = 0  
        self.color("white")  
        self.penup()  
        self.goto(0, 270)  
        self.hideturtle()  
        self.update_scoreboard()  
  
    def update_scoreboard(self):  
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  
  
    def increase_score(self):  
        self.score += 1  
        self.clear()  
        self.update_scoreboard()
```
## Full Code
#### `main.py`:
```py
from turtle import Turtle, Screen  
import time  
from snake import Snake  
from food import Food  
from scoreboard import Scoreboard  
  
screen = Screen()  
screen.setup(width=600, height=600)  
screen.bgcolor("black")  
screen.title("Snake Game")  
screen.tracer(0)  
  
snake = Snake()  
food = Food()  
scoreboard = Scoreboard()  
  
screen.listen()  
screen.onkey(snake.up,"Up")  
screen.onkey(snake.down, "Down")  
screen.onkey(snake.right,"Right")  
screen.onkey(snake.left, "Left")  
  
game_is_on = True  
while game_is_on:  
    screen.update()  
    time.sleep(0.1)  
    snake.move()  
  
    if snake.head.distance(food) < 15:  
        print("nom nom nom")  
        food.refresh()  
        scoreboard.increase_score()  
        snake.increase_length()  
  
    # detect collision with wall  
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:  
        game_is_on = False  
        scoreboard.game_over()  
  
    for segment in snake.segments[1:]:  
        if snake.head.distance(segment) < 10:  
            game_is_on = False  
            scoreboard.game_over()  

  
screen.exitonclick()
```

#### `scoreboard.py`
```py
from turtle import Turtle  
  
  
ALIGNMENT = "center"  
FONT = ("Courier", 24, "normal")  
  
class Scoreboard(Turtle):  
    def __init__(self):  
        super().__init__()  
        self.score = 0  
        self.color("white")  
        self.penup()  
        self.goto(0, 270)  
        self.hideturtle()  
        self.update_scoreboard()  
  
    def update_scoreboard(self):  
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  
  
    def game_over(self):  
        self.goto(0,0)  
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  
    def increase_score(self):  
        self.score += 1  
        self.clear()  
        self.update_scoreboard()
```

#### `food.py`
```py
import random  
from turtle import Turtle  
  
  
class Food(Turtle):  
  
    def __init__(self):  
        super().__init__()  
        self.shape("circle")  
        self.penup()  
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  
        self.color("blue")  
        self.speed("fastest")  
        self.refresh()  
  
    def refresh(self):  
        random_x = random.randint(-280, 280)  
        random_y = random.randint(-280, 280)  
        self.goto(random_x, random_y)
```

#### `snake.py`
```py
from turtle import Turtle  
  
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  
MOVE_DISTANCE = 20  
UP = 90  
DOWN = 270  
RIGHT = 0  
LEFT = 180  
  
  
class Snake:  
    def __init__(self):  
        self.segments = []  
        self.create_snake()  
        self.head = self.segments[0]  
  
    def create_snake(self):  
        for position in STARTING_POSITIONS:  
            self.add_segment(position)  
  
    def add_segment(self, position):  
        new_segment = Turtle("square")  
        new_segment.color("white")  
        new_segment.penup()  
        new_segment.goto(position)  
        self.segments.append(new_segment)  
  
    def increase_length(self):  
        self.add_segment(self.segments[-1].position())  
  
    def move(self):  
        for seg_num in range(len(self.segments) - 1, 0, -1):  
            new_x = self.segments[seg_num - 1].xcor()  
            new_y = self.segments[seg_num - 1].ycor()  
            self.segments[seg_num].goto(new_x, new_y)  
        self.head.forward(MOVE_DISTANCE)  
  
    def up(self):  
        if self.head.heading() != DOWN:  
            self.head.setheading(UP)  
  
    def down(self):  
        if self.head.heading() != UP:  
            self.head.setheading(DOWN)  
  
    def right(self):  
        if self.head.heading() != LEFT:  
            self.head.setheading(RIGHT)  
  
    def left(self):  
        if self.head.heading() != RIGHT:  
            self.head.setheading(LEFT)  
```
