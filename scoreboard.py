from turtle import Turtle

ALIGNMENT = "center"
FONT= ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        # self.pendown()
        self.display_score()

    def display_score(self):
        # self.clear()
        # self.penup()
        # self.goto(0, 270)
        # self.pendown()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.clear()
        self.score += 1
        self.display_score()
