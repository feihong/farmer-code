def go(n):
    for _ in range(n):
        move()

think(10)

width = 0

while not wall_in_front():
    width += 1
    move()

turn_left()
turn_left()
go(width // 2)
put()
