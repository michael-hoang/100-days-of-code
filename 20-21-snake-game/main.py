from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600) # use keyword arguments for clarity
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update() # refresh screen
    time.sleep(0.1) # delay for 0.1 seconds
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    # Detect collision with wall.
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]: # use slicing for more efficient coding
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # for segment in snake.segments:
    #     if segment == snake.head: # Need to exclude snake.head from counting as a segment.
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()



screen.exitonclick()

