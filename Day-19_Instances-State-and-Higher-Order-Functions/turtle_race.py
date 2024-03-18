from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
racers = []
is_race_on = False
quit_racing = False
winner = ""

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    racers.append(new_turtle)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()


while not quit_racing:
    y_pos = -60
    for racer in racers:
        racer.setpos(x=-230, y=y_pos)
        y_pos += 20

    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which turtle will win the race?  Choose a color: ").capitalize()
    if user_bet:
        is_race_on = True
    while is_race_on:
        for racer in racers:
            random_movement = random.randint(0, 10)
            racer.forward(random_movement)
            if racer.xcor() > 230:
                is_race_on = False
                winner = racer.pencolor()

    if user_bet == winner:
        race_again = screen.textinput(title="Checker flag!", prompt=f"{winner} won the race! :) "
                                                                    f"\nGo again? (Y or N)").lower()
    else:
        race_again = screen.textinput(title="Checker flag!", prompt=f"{winner} won the race! :("
                                                                    f"\nGo again? (Y or N)").lower()
    if race_again == "n":
        quit_racing = True
        screen.bye()
