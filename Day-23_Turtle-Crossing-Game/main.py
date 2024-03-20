import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
new_car = CarManager()


screen.listen()
screen.onkey(player.move, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if loop_counter % 6 == 0:
        new_car = CarManager()
    loop_counter += 1


    if player.at_finish_line:
        player.reset_turtle()


# detect when turtle gets hit by car
# detect if turtle reaches finish line
# reset turtle to start and increase car speed