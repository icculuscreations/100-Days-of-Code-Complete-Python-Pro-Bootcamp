from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("SeaGreen3")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.at_finish_line = False

# move turtle north when up key is pressed
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)
        if self.ycor() > FINISH_LINE_Y:
            self.at_finish_line = True

    def reset_turtle(self):
        self.goto(STARTING_POSITION)