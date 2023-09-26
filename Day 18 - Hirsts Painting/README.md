## Challenge 1 -  Draw a square

```py
from turtle import Turtle, Screen  
  
timmy_the_turtle = Turtle()  
timmy_the_turtle.shape("turtle")  
timmy_the_turtle.color("black")  
timmy_the_turtle.forward(100)  
timmy_the_turtle.right(90)  
timmy_the_turtle.forward(100)  
timmy_the_turtle.right(90)  
timmy_the_turtle.forward(100)  
timmy_the_turtle.right(90)  
timmy_the_turtle.forward(100)    
  
screen = Screen()  
screen.exitonclick()
```

## Importing Modules, Installing Packages and Working with Aliases
Some modules have long names. And importing them every single time may be a challenge. Hence, importing the module and using aliases.

```py
import turtle as t

tim = t.Turtle()
```

## Installing packages
Sometimes some packages do not come bundled with python. Some we may have to install from pypi

## Challenge 2 - Drawing a dashed line
```py
import turtle as t

tim = t.Turtle()

for _ in range(15):
	tim.forward(10)
	tim.penup()
	tim.forward(10)
	tim.pendown()

screen = Screen()  
screen.exitonclick()
```

## Challenge 3 - Drawing a triangle, pentagon, hexagon, heptagon, octagon, nonagon and decagon

```py
from turtle import Turtle, Screen  
import random
  
tim = Turtle()  
colours = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat']

num_of_sides = 3  
for __ in range(3, 11):
	tim.color(random.choice(colours))
    for _ in range(num_of_sides):  
        angle = 360 / num_of_sides  
        tim.forward(100)  
        tim.right(angle)  
    num_of_sides += 1  
  
screen = Screen()  
screen.exitonclick()
```

```py
import turtle as t
import random

tim = t.Turtle()

colours = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat']

def draw_shape(num_sides):
	angle = 360 / num_sides
	for _ in range(num_sides):
		tim.forward(100)
		tim.right(angle)

for shape_side_n in range(3, 11):
	tim.color(random.choice(colours))
	drawshape(shape_side_n)
```
## Challenge 4 - Generate a random walk
```py
import turtle as t  
import random  
  
tim = t.Turtle()  
  
colours = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat']  
  
directions = [0, 90, 180, 270]  
  
tim.pensize(7)  
  
tim.speed("fastest")  
  
for _ in range(100):  
    tim.color(random.choice(colours))  
    tim.forward(30)  
    tim.setheading(random.choice(directions))  
  
screen = t.Screen()  
screen.exitonclick()
```

#### Challenge 4 - Generate a random walk, with rgb colors
```py
import turtle as t  
import random  
  
tim = t.Turtle()  
t.colormode(255)  
  
colours = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat']  
  
directions = [0, 90, 180, 270]  
  
tim.pensize(7)  
  
tim.speed("fastest")  
  
for _ in range(100):  
    tim.pencolor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))  
    tim.forward(30)  
    tim.setheading(random.choice(directions))  
  
screen = t.Screen()  
screen.exitonclick()
```

## Challenge 5 - Draw a Spirograph
```py
import turtle as t  
import random  
  
tim = t.Turtle()  
jonny = t.Turtle()  
t.colormode(255)  
  
def random_color():  
    r = random.randint(0, 255)  
    g = random.randint(0, 255)  
    b = random.randint(0, 255)  
    color = (r, g, b)  
    return color  
  
tim.speed("fastest")  
jonny.speed("fastest")  
  
for _ in range(100):  
    tim.color(random_color())  
    tim.circle(100)  
    jonny.setheading(tim.heading())  
    jonny.circle(50)  
    tim.setheading(tim.heading() + 10)
```

# Project - Hirsts Painting
Helper file:
```py colors
import colorgram  
  
colors = colorgram.extract('hirsts_painting.jpeg', 30)  
rgb_colors = []  
  
for color in colors:  
    r = color.rgb.r  
    g = color.rgb.g  
    b = color.rgb.b  
    new_color = (r, g, b)  
    rgb_colors.append(new_color)  
print(rgb_colors)
```

Main
```py
import random  
from colors import rgb_colors  
import turtle as turtle_module  
  
turtle_module.colormode(255)  
tim = turtle_module.Turtle()  
  
def start():
	tim.setheading(225)  
	tim.penup()  
	tim.forward(300)  
	tim.setheading(0)  
  
def linear_draw():  
    tim.setheading(0)  
    for _ in range(10):  
        tim.dot(20, rgb_colors[random.randint(0, 29)])  
        tim.penup()  
        tim.forward(50)  
  
def move_up():  
    tim.backward(50)  
    tim.setheading(90)  
    tim.forward(50)  
  
def linear_draw_right():  
    tim.setheading(180)  
    for _ in range(10):  
        tim.dot(20, rgb_colors[random.randint(0, 29)])  
        tim.penup()  
        tim.forward(50)  
  
def main():
	start()
    for _ in range(5):  
        linear_draw()  
        move_up()  
        linear_draw_right()  
        move_up()  
  
main()  
  
screen = turtle_module.Screen()  
screen.exitonclick()
```

![[download.jpeg]]
