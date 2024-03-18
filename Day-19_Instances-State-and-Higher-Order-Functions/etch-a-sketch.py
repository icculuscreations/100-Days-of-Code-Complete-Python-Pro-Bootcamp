from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_ccw():
    t.left(5)


def turn_cw():
    t.right(5)


def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_ccw)
screen.onkey(key="d", fun=turn_cw)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()