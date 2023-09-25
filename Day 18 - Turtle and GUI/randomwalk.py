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

