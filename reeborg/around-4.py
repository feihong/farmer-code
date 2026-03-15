def go(n):
    for _ in range(n):
        move()

def turn_right():
    for _ in range(3):
        turn_left()

think(10)

width = 0
height = 0

while front_is_clear():
    width += 1
    move()

turn_left()

while front_is_clear():
    height += 1
    move()

turn_left()
turn_left()
go(height // 2)
turn_right()
go(width // 2)
put()
