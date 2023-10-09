import random

import classes

# Returns a random location on the game area that is not inside the snek itself
def get_random_cords(snek_data, window_data):

	cords = [random.randint(0, window_data.width / 10 - 10) * 10, random.randint(0, window_data.height / 10 - 11) * 10]
	while cords in snek_data.body:
		cords = [random.randint(0, window_data.width / 10 - 10) * 10, random.randint(0, window_data.height / 10 - 11) * 10]
	return (cords)

# Creates the wall struct and calculates its position to wall.cords
# needs some sort of pattern not just the same staircase everytime...
def spawn_wall(snek_data, window_data):

	# Starting cordinates for the wall
	start_cords = get_random_cords(snek_data, window_data)

	# Walls cordinate list
	wall_cords = [[start_cords[0], start_cords[1]]]

	# Random length for the wall
	nbr_of_line = random.randint(6, 10)
	line_len = random.randint(10, 14)

	# Wall (wall_cords, length, size)
	wall = classes.wall_struct(wall_cords, nbr_of_line * line_len, snek_data.block_size)

	# Loops for each line and increments the 'block line' towards a random direction
	# and adds the element to wall.cords list
	i = 0
	while i < nbr_of_line:

		direction = random.choice(['N','E','S','W'])
		j = 0
		while j < line_len:

			new_block = wall.cords[-1].copy()
			match direction:
				case 'N':
					new_block[1] -= wall.size
				case 'E':
					new_block[0] += wall.size
				case 'S':
					new_block[1] -= wall.size
				case 'W':
					new_block[0] -= wall.size

			# Portal renderingg for walls
			if new_block[0] < 0:
				new_block[0] = window_data.game_width - wall.size
			elif new_block[0] > window_data.game_width:
				new_block[0] = 0
			if new_block[1] < 0:
				new_block[1] = window_data.game_height - wall.size
			elif new_block[1] > window_data.game_height:
				new_block[1] = 0

			# Prevents the walls from colliding with itself
			if new_block not in wall.cords:
				wall_cords.append(new_block)
			j += 1
		i += 1
	return wall

# Initial spawn location and creation of the snack struct
def spawn_snack(snek_data, window_data):

	starting_cords = get_random_cords(snek_data, window_data)
	snack = classes.snack_struct(starting_cords, snek_data.block_size, False)
	return snack

# Spawns a new snack at a new random location
def update_snack(snek_data, window_data, snack, wall):

	new_snack_cords = get_random_cords(snek_data, window_data)
	# Makes sure snack cannot spawn on top of other game objects
	while new_snack_cords in wall.cords:
		new_snack_cords = get_random_cords(snek_data, window_data)
	snack.cords = new_snack_cords
	snack.spawned = True

# initial spawn location and creation of the power_up struct
def spawn_power_up(snek_data, window_data):

	starting_cords = get_random_cords(snek_data, window_data)
	# random power int(1-2)
	power_type = random.randint(1, 2)
	power_up = classes.power_up_struct(starting_cords, snek_data.block_size, False, power_type)
	return power_up

# Spawns a new power up at a random location
def update_power_up(snek_data, window_data, wall, power_up, snack):

	new_power_up_cords = get_random_cords(snek_data, window_data)
	# Makes sure power_up doesnt spawn on top of a wall
	while new_power_up_cords in snack.cords or new_power_up_cords in wall.cords:
		new_power_up_cords = get_random_cords(snek_data, window_data)
	power_up.cords = new_power_up_cords
	power_up.spawned = True
