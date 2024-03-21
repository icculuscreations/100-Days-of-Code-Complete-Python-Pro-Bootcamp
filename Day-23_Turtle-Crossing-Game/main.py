import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
road = Road()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move_cars()
    loop_counter += 1

    if player.is_at_finish_line():
        scoreboard.current_level += 1
        scoreboard.update_level()
        player.go_to_start()
        cars.increase_car_speed()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

# detect when turtle gets hit by car
# detect if turtle reaches finish line
# reset turtle to start and increase car speed

screen.exitonclick()