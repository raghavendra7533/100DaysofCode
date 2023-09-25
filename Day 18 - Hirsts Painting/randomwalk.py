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
