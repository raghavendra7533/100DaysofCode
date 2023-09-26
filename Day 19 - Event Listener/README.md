## Creating event listeners
```py
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
	tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
```

## Creating Higher Order Functions
```py
def func1(n1, n2):
	return n1 + n2

def func2(n1, n2):
	return n1 - n2

def calculator(n1, n2, func):
	func(n1, n2)

result = calculator(2, 3, add)
print(result) 
# result would be 5
```

## Challenge 1 - Etch a sketch App
The objective was to build an app that recognises the keystrokes and makes the turtle move accordingly. The challenge was to make the turtle move when the keys, "W, A, S, D" were registered. The challenge I faced here was to figure out how to turn the turtle when the key was clicked, since the turtle moves in the angles, directions of the plane which it is in. Hence, to solve this I had to read through the documentation for a while and found out that the `heading` attribute.
```py
from turtle import Turtle, Screen  
  
tim = Turtle()  
screen = Screen()  
  
  
def move_forwards():  
    tim.forward(10)  
  
  
def move_backwards():  
    tim.backward(10)  
  
  
def turn_left():  
    new_heading = tim.heading() + 10  
    tim.setheading(new_heading)  
  
  
def turn_right():  
    new_heading = tim.heading() - 10  
    tim.setheading(new_heading)  
  
  
def clear():  
    tim.clear()  
    tim.penup()  
    tim.home()  
    tim.pendown()  
  
  
screen.listen()  
screen.onkey(key="w", fun=move_forwards)  
screen.onkey(key="s", fun=move_backwards)  
screen.onkey(key="a", fun=turn_left)  
screen.onkey(key="d", fun=turn_right)  
screen.onkey(key="c", fun=clear)  
  
screen.exitonclick()
```

## Turtle Race
#### Importing libraries
```py
from turtle import Turtle, Screen  
import random
```

#### Declaring `is_race_on` to control when the race is starting
```py
is_race_on = False
```

#### Initialising the screen
```py
screen = Screen()  
screen.setup(500, 400)
```

#### Asking the user their bet
```py
user_input = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")
```

#### Declaring the colours of the turtles
```py
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
```

#### Declaring the start positions of the turtles
```py
y_position = [-70, -40, -10, 20, 50, 80]
```

#### Declaring a list to append the turtles
```py
all_turtles = []
```

#### Creating the Turtles
```py
for turtle_index in range(0, 6):  
    new_turtle = Turtle(shape="turtle")  
    new_turtle.color(colors[turtle_index])  
    new_turtle.penup()  
    new_turtle.goto(x=-230, y=y_position[turtle_index])  
    all_turtles.append(new_turtle)
```

#### Starting the race by changing the value of `is_race_on`
```py
if user_input:  
    is_race_on = True
```

#### Logic
```py
while is_race_on: #starting the race only when is_race_on is true
	for turtle in all_turtles: # checking the position of all turtles and declaring the speed of the turtles
		if turtle.xcor() > 230:  
		    is_race_on = False  
		    winning_color = turtle.pencolor()  
		    if winning_color == user_input:  
		        print("You've won!")  
		    else:  
		        print("Better Luck next time.")
    random_distance = random.randint(0,10)  
	turtle.forward(random_distance)
```

## Full Code
```py
from turtle import Turtle, Screen  
import random  
  
  
is_race_on = False  
screen = Screen()  
screen.setup(500, 400)  
user_input = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")  
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  
y_position = [-70, -40, -10, 20, 50, 80]  
all_turtles = []  
  
  
for turtle_index in range(0, 6):  
    new_turtle = Turtle(shape="turtle")  
    new_turtle.color(colors[turtle_index])  
    new_turtle.penup()  
    new_turtle.goto(x=-230, y=y_position[turtle_index])  
    all_turtles.append(new_turtle)  
  
if user_input:  
    is_race_on = True  
  
  
while is_race_on:  
    for turtle in all_turtles:  
        if turtle.xcor() > 230:  
            is_race_on = False  
            winning_color = turtle.pencolor()  
            if winning_color == user_input:  
                print("You've won!")  
            else:  
                print("Better Luck next time.")  
        random_distance = random.randint(0,10)  
        turtle.forward(random_distance)  
  
  
screen.exitonclick()
```