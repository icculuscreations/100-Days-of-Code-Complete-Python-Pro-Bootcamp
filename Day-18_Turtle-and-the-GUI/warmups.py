import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
# t.shape("turtle")
# t.color("DarkOliveGreen4")
screen.screensize(1000, 1000)
turtle.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# draw a dashed line
# t.teleport(-400, 0)
# for _ in range(40):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# draw shapes
# def draw_shapes():
#     """Draws triangles, square, pentagon, etc..."""
#     for i in range(3, 11):
#         color = random.choice(available_colors)
#         t.color(color)
#         sides = i
#         angle = 360 / sides
#         for _ in range(sides):
#             t.fd(100)
#             t.rt(angle)
#
#
# draw_shapes()


# draw a random walk
# directions = [0, 90, 180, 270]
# t.width(10)
# t.speed("fastest")
# for _ in range(1000):
#     t.color(random_color())
#     t.setheading(random.choice(directions))
#     t.forward(20)


# draw a spirograph
# angle = 10
# turns = int(360 / angle)
# t.speed("fastest")
# t.width(5)
# for _ in range(turns):
#     t.color(random_color())
#     t.circle(150)
#     t.left(angle)


screen.exitonclick()

