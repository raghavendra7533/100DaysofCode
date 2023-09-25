from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat']

num_of_sides = 3
for __ in range(10):
    tim.color(random.choice(colours))
    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        tim.forward(100)
        tim.right(angle)
    num_of_sides += 1

screen = Screen()
screen.exitonclick()