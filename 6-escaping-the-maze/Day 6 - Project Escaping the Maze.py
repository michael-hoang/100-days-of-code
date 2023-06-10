def turn_right():
    for _ in range(3):
        turn_left()

# Move robot towards a wall and out of the position where infinite loops occurs.
while front_is_clear():
    move()
turn_left()

# Algorithm to move robot towards goal.        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
