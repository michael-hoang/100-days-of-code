from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinate : tuple):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(coordinate)
        
    def move_up(self):
       new_y = self.ycor() + 25
       self.goto(self.xcor(), new_y)

    def move_down(self):
       new_y = self.ycor() - 25
       self.goto(self.xcor(), new_y)

