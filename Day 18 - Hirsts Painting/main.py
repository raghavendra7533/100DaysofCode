import random
from colors import rgb_colors
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()

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
    for _ in range(5):
        linear_draw()
        move_up()
        linear_draw_right()
        move_up()

main()

screen = turtle_module.Screen()
screen.exitonclick()
