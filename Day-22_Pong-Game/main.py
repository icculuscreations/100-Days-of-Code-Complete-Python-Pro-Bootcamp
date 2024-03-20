from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Classic Game - Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()













screen.exitonclick()