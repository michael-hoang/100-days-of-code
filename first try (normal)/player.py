"""Module contains class modeling the player as a turtle."""

from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """A simple representation of the palyer as a turtle."""
    def __init__(self):
        super().__init__("turtle")
        self.setheading(90)
        self.penup()
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)      

    def move(self):
        self.forward(MOVE_DISTANCE)  

    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False