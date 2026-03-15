def go(n):
    for _ in range(n):
        move()

def turn_right():
    for _ in range(3):
        turn_left()

think(10)

move()

while not at_goal():
    if wall_in_front():
        turn_left()

    if object_here():
        take()

    move()
