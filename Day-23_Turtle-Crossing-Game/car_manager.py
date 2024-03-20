from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.new_car()

    def move_car(self):
        while self.xcor() > -300:
            new_x = self.xcor() - STARTING_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def new_car(self):
        self.color(random.choice(COLORS))
        self.goto(x=300, y=random.randrange(-280, 280, 20))
        self.move_car()

    def increase_car_speed(self):
        pass
