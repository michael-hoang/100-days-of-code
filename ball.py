from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("orange")
        self.penup()
        self.x_move_step = 10
        self.y_move_step = 5
        self.move_speed = 0.1

    def first_serve(self):
        """Starts the game with ball moving in a random direction."""
        direction = [1, -1]
        choose_direction_x = random.choice(direction)
        choose_direction_y = random.choice(direction)

        self.x_move_step = self.x_move_step * choose_direction_x
        self.y_move_step = self.y_move_step * choose_direction_y

        self.move()

    def move(self):
        x = self.xcor() + self.x_move_step
        y = self.ycor() + self.y_move_step
        self.goto(x, y)

    def bounce_y(self):
        self.y_move_step *= -1

    def bounce_x(self):
        self.x_move_step *= -1
        # Ball moves faster with each bounce on paddle.
        self.move_speed /= 1.2

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        # self.x_move *= -1
        self.bounce_x()
        self.move_speed = 0.1
