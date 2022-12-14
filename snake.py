from turtle import Turtle

# Global constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = [] # the attribute 'self.segments' is a list.
        self.create_snake() # gets called when object gets initialized.
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
 
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # The idea is that each segment (starting from the last) is following the leader,
        # therefore, the snake's head has to be the last piece to move.
        for segment_index in range(len(self.segments) - 1, 0, -1): # index 0 is not inclusive
            new_x = self.segments[segment_index - 1].xcor()
            new_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE) # need this line b/c index 0 is exclusive

    def up(self):
        """Snake turns 90 degrees north."""
        # self.head_direction = self.head.heading()
        # if self.head_direction == 0:
        #     self.head.setheading(self.head_direction + 90)
        # elif self.head_direction == 180:
        #     self.head.setheading(self.head_direction - 90)

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Snake turns 90 degrees south."""
        # self.head_direction = self.head.heading()
        # if self.head_direction == 0:
        #     self.head.setheading(self.head_direction - 90)
        # elif self.head_direction == 180:
        #     self.head.setheading(self.head_direction + 90)

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Snake turns 90 degrees west."""
        # self.head_direction = self.head.heading()
        # if self.head_direction == 90:
        #     self.head.setheading(self.head_direction + 90)
        # elif self.head_direction == 270:
        #     self.head.setheading(self.head_direction - 90)

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Snake turns 90 degrees east."""
        # self.head_direction = self.head.heading()
        # if self.head_direction == 90:
        #     self.head.setheading(self.head_direction - 90)
        # elif self.head_direction == 270:
        #     self.head.setheading(self.head_direction + 90)

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


