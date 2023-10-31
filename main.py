from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()


def colour():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


timmy.speed(100)
timmy.pensize(1)

for _ in range(180):
    timmy.pencolor(colour())
    timmy.circle(100)
    timmy.left(4)


screen = Screen()
screen.exitonclick()
