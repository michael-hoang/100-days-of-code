import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player turtle object.
player = Player()

# Create scoreboard object.
scoreboard = Scoreboard()

# Bind "Up" key to move():
screen.listen()
screen.onkeypress(player.move, "Up")

# Create car manager object.
carmanager = CarManager()


game_is_on = True
loop_counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Produce a car every 6 loops.
    if loop_counter % 6 == 0:
        carmanager.produce_car()

    # # Alternatively....program a six-sided die.
    # random_chance = random.randint(1, 6)
    # if random_chance == 1:
    #     carmanager.produce_car()

    # Level up
    if player.check_finish_line():
        player.reset_position()
        scoreboard.increment_score()
        scoreboard.display_level()
        carmanager.increase_speed()
    
    carmanager.move()

    # Remove excess car that left the screen.
    carmanager.remove_car()
    
    # Collision with car.
    for car in carmanager.garage:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    loop_counter += 1

  
screen.exitonclick()