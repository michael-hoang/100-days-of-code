import turtle
import random

# import colorgram

# colors = colorgram.extract('image.jpg', 35)

# extracted_colors = []

# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb = (r, g, b)
#     extracted_colors.append(rgb)

# print(extracted_colors)

color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
    (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
    (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
    (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
    (254, 194, 0)
    ]

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
turtle.colormode(255)

def paint_horizontal(row_length):
    """Paint 10 random color dots."""
    for _ in range(row_length):
        my_turtle.dot(20,random.choice(color_list))
        my_turtle.forward(50)

def new_row(starting_x_position):
    """Move turtle up to beginning of new row."""
    my_turtle.setx(starting_x_position)
    current_y = my_turtle.ycor()
    my_turtle.sety(current_y + 50)

length = int(input("Enter length between 1 and 20: "))
total_dots = length**2

set_start_x = my_turtle.setx(-length * 50 / 2)
set_start_y = my_turtle.sety(-length * 50 / 2)
starting_x = my_turtle.xcor()

for _ in range(length):
    paint_horizontal(length)
    new_row(starting_x)

screen = turtle.Screen()
screen.exitonclick()
