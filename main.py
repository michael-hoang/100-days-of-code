from turtle import Screen
from time import sleep

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
# screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()

    if ball.xcor() == 0 and ball.ycor() == 0 and scoreboard.left_score == 0 \
            and scoreboard.right_score == 0:
        ball.first_serve()
    ball.move()

    # Detect wall bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < \
            -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Detect ball going out of right bound.
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset()

    # Detect ball going out of left bound.
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset()

screen.exitonclick()
