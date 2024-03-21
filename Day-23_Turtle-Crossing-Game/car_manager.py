from turtle import Turtle
import random

COLORS = ["firebrick", "DarkOrange3", "gold1", "LawnGreen", "DodgerBlue1", "DarkOrchid4"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 0.5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.add_car()

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randrange(-240, 260, 20))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_car_speed(self):
        for car in self.all_cars:
            self.car_speed += MOVE_INCREMENT
