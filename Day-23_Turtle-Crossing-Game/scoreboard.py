from turtle import Turtle

LEVEL_FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.update_level()

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, -290)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)

    def update_level(self):
        self.clear()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-210, -290)
        self.write(f"Level: {self.current_level}", align="center", font=LEVEL_FONT)


# create a scoreboard that shows what level the player is on
# if turtle gets hit, print GAME OVER at middle of screen
