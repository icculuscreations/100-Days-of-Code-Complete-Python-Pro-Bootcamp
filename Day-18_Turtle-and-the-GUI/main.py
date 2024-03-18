from get_colors import painting_colors

import turtle
from turtle import Turtle, Screen
import random

GRID_H = 10
GRID_W = 10
DOT_SIZE = 20
DOT_SPACING = 50
STARTING_X = -250
STARTING_Y = -250

t = Turtle()
screen = Screen()
screen.screensize(100, 100)
turtle.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

t.teleport(STARTING_X, STARTING_Y)
for i in range(GRID_H):
    for _ in range(GRID_W):
        t.dot(DOT_SIZE, random.choice(painting_colors))
        t.fd(DOT_SPACING)
    t.setx(STARTING_X)
    t.sety(STARTING_Y + ((i + 1) * DOT_SPACING))


screen.exitonclick()
