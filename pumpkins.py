# Grow pumpkins more efficiently grouping them into a quadrant, making it more
# likely that they'll merge into larger pumpkins

wsize = get_world_size()

def water():
	if get_water() < 0.9 and num_items(Items.Water) > 0:
			use_item(Items.Water)

def reset_position():
    x = get_pos_x()
    y = get_pos_y()
    for _ in range(x):
        move(West)
    for _ in range(y):
        move(South)

def handle_pumpkin():
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Pumpkin)

def handle_tree_or_bush(x, y):
    if (x + y) % 2 == 0:
        plant(Entities.Bush)
    else:
        plant(Entities.Tree)

def handle_carrot():
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Carrot)

def handle(x, y):
    # print(x, y)
    water()

    if can_harvest():
        harvest()

    if x < 6 and y < 6:
        handle_pumpkin()
    elif x < 6 and y < 12:
        handle_tree_or_bush(x, y)
    elif y < 6:
        handle_carrot()
    else:
        pass # grass

def sweep():
    for x in range(wsize):
        for y in range(wsize):
            handle(x, y)
            move(North)
        move(East)

clear()

while True:
    sweep()
