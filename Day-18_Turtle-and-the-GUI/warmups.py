from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("DarkOliveGreen4")

# draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

screen = Screen()
screen.exitonclick()

