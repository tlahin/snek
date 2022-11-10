import random

import classes

def spawn_wall(snek_data, window_data):

    start_cords = [random.randint(0, window_data.width / 10 - 10) * 10, random.randint(0, window_data.height / 10 - 11) * 10]
    wall_cords = [[start_cords[0], start_cords[1]]]
	# Wall (window_data, size, length, colour)
    wall = classes.wall_struct(wall_cords, 5, snek_data.block_size, 'red')
    j = 0

    while j < wall.length:

        new_block = wall.cords[j].copy()
        for i in range(len(new_block)):
            new_block[i] += snek_data.block_size
        wall.cords.append(new_block)
        j += 1
    return wall

def spawn_snack(snek_data, window_data, wall):

    starting_cords = [random.randint(0, window_data.width / 10 - 10) * 10, random.randint(0, window_data.height / 10 - 11) * 10]
    snack = classes.snack_struct(starting_cords, snek_data.block_size, 'green', False, wall)
    return snack

def update_snack(snack, window_data):

    i = [random.randint(0, window_data.width / 10 - 10) * 10, random.randint(0, window_data.height / 10 - 11) * 10]
    # Makes sure snack cannot spawn on top of a wall
    if i not in snack.wall.cords:
        snack.cords = i
    snack.spawned = True