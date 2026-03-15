def go(n):
    for _ in range(n):
        move()

def turn_right():
    for _ in range(3):
        turn_left()

for i in range(4):
    if i != 0:
        turn_right()
        move()
        turn_right()
    go(3)
    turn_left()
    go(3)
