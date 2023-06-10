"""This module contains a class that models a car manager."""

from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """A simple representation of a car manager."""

    def __init__(self):
        self.garage = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def produce_car(self):
        new_car = Turtle("square")
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        new_car.shapesize(stretch_len=2)
        new_car.setheading(180)
        new_car.speed = self.speed
        new_car.color(random.choice(COLORS))
        self.garage.append(new_car)

    def move(self):
        for car in self.garage:
            car.forward(self.speed)

    def increase_speed(self):
            self.speed += MOVE_INCREMENT

    def remove_car(self):
        for car in self.garage:
            if car.xcor() < -320:
                self.garage.remove(car)
                car.hideturtle()


