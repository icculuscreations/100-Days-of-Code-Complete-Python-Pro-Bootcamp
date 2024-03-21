from turtle import Turtle, Screen


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.y_position = 250
        for _ in range(26):
            self.draw_lane()
        self.draw_bushes()

    def draw_lane(self):
        self.color("black")
        self.penup()
        self.goto(-310, self.y_position)
        self.pendown()
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.y_position -= 20

    def draw_bushes(self):
        self.hideturtle()
        self.penup()
        self.goto(-310, 280)
        for _ in range(31):
            self.dot(20, "DarkGreen")
            self.forward(20)
