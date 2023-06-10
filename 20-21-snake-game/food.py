from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Halve the length and width.
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 200)

        random_x = random.randrange(-280, 281, 20) # .randrange(n1, n2, 20) gives better precision than .randint(n1, n2)
        random_y = random.randrange(-280, 281, 20) # because Snake's MOVE_DISTANCE = 20.
        self.goto(random_x, random_y)
