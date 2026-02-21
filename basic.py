"""
Very basic script that only grows bushes, trees, carrots, and pumpkins (inefficiently)
"""

def water():
	if get_water() < 0.9 and num_items(Items.Water) > 0:
			use_item(Items.Water)

while True:
	move(East)
	x = get_pos_x()
	for i in range(get_world_size()):
		move(North)
		y = get_pos_y()
		water()

		if can_harvest():
			harvest()

		if x == y: # on diagonal
			plant(Entities.Tree)
		elif x == 0:
			plant(Entities.Bush)
		elif x == 1:
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Carrot:
				plant(Entities.Carrot)
		elif x == 5:
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
