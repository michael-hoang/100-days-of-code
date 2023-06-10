"""This module contains class that models a scoreboard."""

from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """A simple representation of a scoreboard."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increment_score(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "bold"))