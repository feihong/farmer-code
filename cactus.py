# Like sunflower but also grow cactus

wsize = get_world_size()

def water():
	if get_water() < 0.9 and num_items(Items.Water) > 0:
			use_item(Items.Water)

def handle_tree_or_bush(x, y):
    if (x + y) % 2 == 0:
        plant(Entities.Bush)
    else:
        plant(Entities.Tree)

def move_to(x, y):
    x1 = get_pos_x()
    y1 = get_pos_y()
    if x < x1:
        dir = West
    else:
        dir = East
    for _ in range(abs(x - x1)):
        move(dir)
    if y < y1:
        dir = South
    else:
        dir = North
    for _ in range(abs(y - y1)):
        move(dir)

def till_square(x, y):
    if x < 6 and y < 6:
        till()
    elif x > 7:
        till()

def farm_square(x, y):
    water()

    if can_harvest():
        harvest()

    if x < 6 and y < 6:
        plant(Entities.Pumpkin)
    elif x < 6 and y < 12:
        handle_tree_or_bush(x, y)
    elif x < 8:
        # grass
        pass
    elif x < 10:
        plant(Entities.Carrot)
    elif x == 10:
        plant(Entities.Sunflower)
    elif x == 11:
        plant(Entities.Cactus)

# Run square_fn on every square of the farm
def sweep(square_fn):
    for x in range(wsize):
        for y in range(wsize):
            square_fn(x, y)
            move(North)
        move(East)

clear()
sweep(till_square)

while True:
    sweep(farm_square)
