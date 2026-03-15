def go(n):
    for _ in range(n):
        move()

def turn_right():
    for _ in range(3):
        turn_left()

think(10)

put()
move()

while not object_here():
    if wall_in_front():
        turn_left()

    move()
