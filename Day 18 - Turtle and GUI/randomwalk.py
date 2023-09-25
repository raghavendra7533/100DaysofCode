import turtle as t
import random

tim = t.Turtle()

colours = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat']

directions = [0, 90, 180, 270]

for _ in range(20):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

